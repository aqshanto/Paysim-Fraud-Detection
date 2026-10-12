"""Compare models with and without the PaySim balance attributes (paper Section 5.8, Table 16).

Run from the repository root:  python scripts/balance_comparison.py
Writes results/balance_comparison_results.json. Takes about 30 minutes (random forest is the slowest part).
"""
import json
import time
from pathlib import Path

import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'paysim_raw.csv'
OUT = ROOT / 'results' / 'balance_comparison_results.json'

FEATURE_SETS = {
    'with_balance': ['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest',
                     'empties_amount', 'is_whole', 'dest_zero', 'hour'],
    'without_balance': ['type', 'amount', 'is_whole', 'hour'],
}
MODELS = {
    'LR': lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    'HGB_L2': lambda: HistGradientBoostingClassifier(random_state=42, l2_regularization=1.0),
    'RF': lambda: RandomForestClassifier(n_estimators=100, n_jobs=2, random_state=42),
}


def load():
    cols = ['step', 'type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFraud']
    df = pd.read_csv(DATA, usecols=cols)
    d = df[df['type'].isin(['TRANSFER', 'CASH_OUT'])].copy()
    d['empties_amount'] = (d['amount'] == d['oldbalanceOrg']).astype(int)
    d['is_whole'] = (d['amount'] % 1 == 0).astype(int)
    d['dest_zero'] = ((d['oldbalanceDest'] == 0) & (d['newbalanceDest'] == 0)).astype(int)
    d['hour'] = d['step'] % 24
    d['type'] = (d['type'] == 'TRANSFER').astype(int)
    return d


def main():
    t0 = time.time()
    d = load()
    y = d['isFraud']
    chrono = d['step'] <= d['step'].quantile(0.8)
    splits = {
        'random': train_test_split(d.index, test_size=0.2, stratify=y, random_state=42),
        'chronological': (d.index[chrono], d.index[~chrono]),
    }
    results = []
    for fs, feats in FEATURE_SETS.items():
        for split, (tr, te) in splits.items():
            X_tr, X_te = d.loc[tr, feats].astype('float32'), d.loc[te, feats].astype('float32')
            y_tr, y_te = y.loc[tr], y.loc[te]
            for name, make_model in MODELS.items():
                model = make_model().fit(X_tr, y_tr)
                prob = model.predict_proba(X_te)[:, 1]
                pred = (prob >= 0.5).astype(int)
                tn, fp, fn, tp = confusion_matrix(y_te, pred).ravel()
                row = dict(features=fs, split=split, model=name,
                           precision=precision_score(y_te, pred, zero_division=0), recall=recall_score(y_te, pred),
                           f1=f1_score(y_te, pred), pr_auc=average_precision_score(y_te, prob),
                           false_alarms=int(fp), missed=int(fn), test_frauds=int(y_te.sum()))
                if name == 'RF':
                    row['avg_tree_nodes'] = int(sum(t.tree_.node_count for t in model.estimators_) / len(model.estimators_))
                results.append(row)
                print({k: round(v, 4) if isinstance(v, float) else v for k, v in row.items()}, flush=True)
    OUT.write_text(json.dumps(results, indent=1))
    print(f'saved {OUT} in {time.time() - t0:.0f}s')


if __name__ == '__main__':
    main()
