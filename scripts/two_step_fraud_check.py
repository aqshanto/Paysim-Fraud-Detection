"""Check the two-step TRANSFER -> CASH_OUT fraud pattern (hypothesis H7) and its effect on data splitting
(paper Section 3.3, Table 7, and the group-aware split in Table 10).

Run from the repository root:  python scripts/two_step_fraud_check.py
Takes about 5 minutes.
"""
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'paysim_raw.csv'
FEATURES = ['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest',
            'empties_amount', 'is_whole', 'dest_zero', 'hour']


def match_share(transfers, cashouts):
    keys = set(zip(cashouts['step'], cashouts['amount']))
    hits = [k in keys for k in zip(transfers['step'], transfers['amount'])]
    return sum(hits), len(hits)


def main():
    t0 = time.time()
    df = pd.read_csv(DATA)
    d = df[df['type'].isin(['TRANSFER', 'CASH_OUT'])].copy()
    del df

    fraud, legit = d[d['isFraud'] == 1], d[d['isFraud'] == 0]
    ft, fc = fraud[fraud['type'] == 'TRANSFER'], fraud[fraud['type'] == 'CASH_OUT']
    lt, lc = legit[legit['type'] == 'TRANSFER'], legit[legit['type'] == 'CASH_OUT']

    print('account chain (fraud TRANSFER receiver == fraud CASH_OUT sender):',
          len(set(ft['nameDest']) & set(fc['nameOrig'])))
    k, n = match_share(ft, fc)
    print(f'fraud TRANSFER with a fraud CASH_OUT at same step + amount: {k} / {n} ({k / n:.2%})')
    k, n = match_share(lt, lc)
    print(f'control, legitimate TRANSFER with legitimate CASH_OUT:      {k} / {n} ({k / n:.4%})')

    # features
    d['empties_amount'] = (d['amount'] == d['oldbalanceOrg']).astype(int)
    d['is_whole'] = (d['amount'] % 1 == 0).astype(int)
    d['dest_zero'] = ((d['oldbalanceDest'] == 0) & (d['newbalanceDest'] == 0)).astype(int)
    d['hour'] = d['step'] % 24
    d['type'] = (d['type'] == 'TRANSFER').astype(int)
    X, y = d[FEATURES], d['isFraud']

    # random split vs. group-aware split (both legs of a fraud pair kept together)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    is_fr = d['isFraud'] == 1
    gid = pd.Series(np.arange(len(d)), index=d.index)
    codes = pd.factorize(d.loc[is_fr, 'step'].astype(str) + '_' + d.loc[is_fr, 'amount'].astype(str))[0]
    gid[is_fr] = len(d) + codes
    uniq = gid.unique()
    rng = np.random.RandomState(42)
    g_test = gid.isin(set(uniq[rng.rand(len(uniq)) < 0.2]))

    models = {
        'LR': lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
        'HGB default': lambda: HistGradientBoostingClassifier(random_state=42),
        'RF': lambda: RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42),
    }
    print(f"\n{'model':12s} F1 random  F1 group-aware")
    print(f"{'Rule':12s} {f1_score(y_te, X_te['empties_amount']):.4f}     {f1_score(y[g_test], X[g_test]['empties_amount']):.4f}")
    for name, make_model in models.items():
        f_r = f1_score(y_te, make_model().fit(X_tr, y_tr).predict(X_te))
        f_g = f1_score(y[g_test], make_model().fit(X[~g_test], y[~g_test]).predict(X[g_test]))
        print(f'{name:12s} {f_r:.4f}     {f_g:.4f}', flush=True)
    print(f'\ndone in {time.time() - t0:.0f}s')


if __name__ == '__main__':
    main()
