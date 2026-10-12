# Data

The dataset is **not** included in this repository (about 494 MB).

1. Download *Synthetic Financial Datasets For Fraud Detection* (PaySim, version 2) from Kaggle:
   https://www.kaggle.com/datasets/ealaxi/paysim1
2. Unzip it and save the CSV in this folder as:

```
data/paysim_raw.csv
```

The file has 6,362,620 rows and 11 columns
(`step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest, newbalanceDest, isFraud, isFlaggedFraud`).

## Important note on the balance columns

The dataset documentation states that transactions detected as fraud are cancelled, and that the four balance columns
(`oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`) should therefore not be used for fraud detection.
This project analyses these columns on purpose and reports results **with and without** them
(see `scripts/balance_comparison.py` and Section 5.8 of the paper).
