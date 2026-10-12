# Reading list: PaySim / mobile money fraud detection paper

All papers below were found as **open access**. Each link opens the paper's page on Consensus; from there use the "PDF" / publisher link to download.
**Before citing any paper, open it and check the details yourself** (authors, year, venue, numbers).

- **Tier 1 = read fully yourself (10 papers).** These shape the paper's argument.
- **Tier 2 = skim / summarize with NotebookLM.** Check every claim you use against the PDF.
- Venue quality varies. For the Related Work text, lean on well-known venues (IEEE, Elsevier, Springer, Nature, etc.). The weaker PaySim papers are still useful as evidence for the "published PaySim results" table.

Reading tracker: change `[ ]` to `[x]` when done.

---

## Tier 1: read fully (10)

| Done | # | Paper | Why it matters for our paper |
|---|---|---|---|
| [ ] | 1 | [Advantages of the PaySim Simulator for Improving Financial Fraud Controls](https://consensus.app/papers/details/dcca3ffd625c5363aa64ba29d149306a/?utm_source=claude_desktop) (Lopez-Rojas et al., 2019, Advances in Intelligent Systems and Computing) | The dataset's own authors: how PaySim generates data and fraud. Needed for Section 3. |
| [ ] | 2 | [Predicting mobile money transaction fraud using machine learning algorithms](https://consensus.app/papers/details/52ef6a092d0c58d9a239a3fb583d2a92/?utm_source=claude_desktop) (Lokanan, 2023, Applied AI Letters) | Mobile money fraud, LR baseline vs ensembles. Close to our design. |
| [ ] | 3 | [Fraud Detection in Mobile Payment Systems using an XGBoost-based Framework](https://consensus.app/papers/details/bed4c5fd8590584a949d5166186e7293/?utm_source=claude_desktop) (Hájek et al., 2022, Information Systems Frontiers, 182 cit.) | Strong-venue study on >6M mobile transactions, imbalance + cost view. Key comparison paper. |
| [ ] | 4 | [Fraud Detection in Financial Transactions Using ML: Insights from the PaySim Mobile Money Dataset](https://consensus.app/papers/details/465951e291e4509cb8c6b7da1d44e4c2/?utm_source=claude_desktop) (Alumona et al., 2025) | Same dataset, feature engineering, stratified 80:20 split. Directly comparable to our work. |
| [ ] | 5 | [Financial Fraud Detection Based on Machine Learning: A Systematic Literature Review](https://consensus.app/papers/details/b9f78c911fa85f409d789f3c13acbfcd/?utm_source=claude_desktop) (Ali et al., 2022, Applied Sciences, 400 cit.) | Backbone of Related Work: which ML methods and metrics the field uses. |
| [ ] | 6 | [Financial fraud detection through the application of machine learning techniques: a literature review](https://consensus.app/papers/details/a1f2281d8b2054fcaf63a4da41b1c6fb/?utm_source=claude_desktop) (Hernández Aros et al., 2024, Humanities and Social Sciences Communications) | Reports synthetic data is used in <7% of studies. Useful for motivating our synthetic-data discussion. |
| [ ] | 7 | [Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy](https://consensus.app/papers/details/9397d1bf42a2593b8b19c0b7787595ca/?utm_source=claude_desktop) (Dal Pozzolo et al., 2018, IEEE TNNLS, 598 cit.) | Classic paper on realistic evaluation, concept drift, proper metrics. Supports our chronological split. |
| [ ] | 8 | [Leakage and the reproducibility crisis in machine-learning-based science](https://consensus.app/papers/details/f7b850c06abb58db8d431f9ce35d007c/?utm_source=claude_desktop) (Kapoor et al., 2023, Patterns, 1201 cit.) | Shows complex ML often isn't better than LR once evaluation is fixed. Parallel to our rule-vs-ML finding. |
| [ ] | 9 | [Feature engineering strategies for credit card fraud detection](https://consensus.app/papers/details/3af3ee3c7c615e19bb31f1918afa6f54/?utm_source=claude_desktop) (Correa Bahnsen et al., 2016, Expert Systems with Applications, 441 cit.) | Foundational feature-engineering paper (aggregation, time features). Supports our Section 4.2. |
| [ ] | 10 | [Data engineering for fraud detection](https://consensus.app/papers/details/ecfd82e8231e58b08917988d3b4d6dba/?utm_source=claude_desktop) (Baesens et al., 2021, Decision Support Systems, 161 cit.) | Feature/instance engineering while keeping models interpretable. Matches our "simple features" message. |

---

## Tier 2: skim / NotebookLM

### A. PaySim and mobile money fraud studies (for the "published PaySim results" table)

| Done | # | Paper | Note |
|---|---|---|---|
| [ ] | 11 | [Social simulation of commercial and financial behaviour for fraud detection research](https://consensus.app/papers/details/b0ee212001ed5a28ae98aa4237dfac43/?utm_source=claude_desktop) (Lopez-Rojas et al., 2014) | PaySim, RetSim, BankSim origins |
| [ ] | 12 | [On the Simulation of Financial Transactions for Fraud Detection Research](https://consensus.app/papers/details/7934e18511a25f5a878e716750a568d9/?utm_source=claude_desktop) (Lopez-Rojas, 2014, PhD thesis) | Notes simple threshold detection was already effective. Relevant to our rule baseline. |
| [ ] | 13 | [Multi Agent Based Simulation (MABS) of Financial Transactions for AML](https://consensus.app/papers/details/7f3ec3325c99508f8f7bfd974612fa15/?utm_source=claude_desktop) (Lopez-Rojas et al., 2012) | Early PaySim design |
| [ ] | 14 | [Explainable AI-enhanced ensemble learning for financial fraud detection in mobile money transactions](https://consensus.app/papers/details/4042c766125254ff9e7284adb8475459/?utm_source=claude_desktop) (Vijayanand et al., 2024, Intelligent Decision Technologies) | PaySim, voting ensemble, 99.9% accuracy, SHAP |
| [ ] | 15 | [Optimized Feature Engineering for Transaction Fraud Detection Using Sequential and HMM-Based Features](https://consensus.app/papers/details/de5dff22efcc54bc8f8e3204afd6e8a2/?utm_source=claude_desktop) (Thar et al., 2025) | Same filtering as ours (2.77M, 0.2965% fraud). Good comparison. |
| [ ] | 16 | [Hybrid Feature Engineering Based on Customer Spending Behavior for Credit Card Anomaly and Fraud Detection](https://consensus.app/papers/details/990049f6fdd55dd18d3c26b57941d154/?utm_source=claude_desktop) (Alamri et al., 2024, Electronics) | Feature aggregation + selection on PaySim |
| [ ] | 17 | [Enhancing credit card fraud detection using traditional and deep learning models with class imbalance mitigation](https://consensus.app/papers/details/3e7e09421a1a57b791e3c6d108e4c225/?utm_source=claude_desktop) (Albalawi & Dardouri, 2025, Frontiers in AI) | Uses both the Kaggle credit card data and PaySim |
| [ ] | 18 | [A Comparative Evaluation of ML Algorithms for Anomaly Detection in Mobile Money Transactions](https://consensus.app/papers/details/4d70d5f16e3e50a9a45c244f09d920d9/?utm_source=claude_desktop) (Ekedebe, 2026) | PaySim, SMOTE, low precision reported |
| [ ] | 19 | [Pattern Recognition for Fraud Detection in Mobile Money Transactions in Nigeria using a Stacked Ensemble](https://consensus.app/papers/details/e3ffc57eaad75267a5f59044303ffefc/?utm_source=claude_desktop) (Ogwueleka et al., 2025) | PaySim, undersampling, stacked ensemble |
| [ ] | 20 | [Application of ML Models for Fraud Detection in Synthetic Mobile Financial Transactions](https://consensus.app/papers/details/673d23a4512555419faba4c1c987da8e/?utm_source=claude_desktop) (Mulyana et al., 2025) | PaySim, CRISP-DM workflow (useful for our workflow figure idea) |
| [ ] | 21 | [Financial Fraud Identification Using Deep Learning Techniques](https://consensus.app/papers/details/4377a8debcd655d583f59f85c6559a47/?utm_source=claude_desktop) (Nama et al., 2024) | PaySim, RNN, 99.87% accuracy |
| [ ] | 22 | [Fraud Detection in Mobile Money Transactions Using Machine Learning](https://consensus.app/papers/details/d11966abde0657e29549c18fc3fe9939/?utm_source=claude_desktop) (Kang, 2019) | RF vs gradient boosting on mobile money data |
| [ ] | 23 | [Deep Learning Approaches for Anti-Money Laundering on Mobile Transactions: Review, Framework, and Directions](https://consensus.app/papers/details/4ff839f13b435e2ab271b7365c3e8aa7/?utm_source=claude_desktop) (Fan et al., 2025, IEEE Internet of Things Journal) | Mobile-payment AML review |
| [ ] | 24 | [Scenario-based Synthetic Dataset Generation for Mobile Money Transactions](https://consensus.app/papers/details/cf8e433795e5598599fe63f8c2ab22f8/?utm_source=claude_desktop) (Azamuke et al., 2022) | Compares PaySim, AMLSim, others. Proposes MoMTSim |
| [ ] | 25 | [A labeled synthetic mobile money transaction dataset](https://consensus.app/papers/details/d825195555b75e859020713f93c95361/?utm_source=claude_desktop) (Azamuke et al., 2025, Data in Brief) | MoMTSim dataset, same columns as PaySim. Candidate second dataset for future work |

### B. Reviews of financial fraud detection

| Done | # | Paper | Note |
|---|---|---|---|
| [ ] | 26 | [Deep Learning in Financial Fraud Detection: Innovations, Challenges, and Applications](https://consensus.app/papers/details/dd3610c8810e573e854d79eb651c877e/?utm_source=claude_desktop) (Chen et al., 2025, Data Science and Management) | 108 papers reviewed |
| [ ] | 27 | [A systematic review of AI-enhanced techniques in credit card fraud detection](https://consensus.app/papers/details/eaf15ccebf8b52ada8710cc56f1ec053/?utm_source=claude_desktop) (Hafez et al., 2025, Journal of Big Data) | Credit card focus |
| [ ] | 28 | [AI Driven Fraud Detection Models in Financial Networks: A Comprehensive Systematic Review](https://consensus.app/papers/details/78aea2c123e8576faa9019a8db2737bf/?utm_source=claude_desktop) (Sarna et al., 2025, IEEE Access) | Taxonomy of methods |

### C. Class imbalance

| Done | # | Paper | Note |
|---|---|---|---|
| [ ] | 29 | [Performance Evaluation of ML Methods for Credit Card Fraud Detection using SMOTE and AdaBoost](https://consensus.app/papers/details/a44ea91bfec65ed595b21587a289f834/?utm_source=claude_desktop) (Ileberi et al., 2021, IEEE Access, 200 cit.) | SMOTE baseline |
| [ ] | 30 | [The effect of feature extraction and data sampling on credit card fraud detection](https://consensus.app/papers/details/d72bfb06098059d89e2ff8905ff587af/?utm_source=claude_desktop) (Salekshahrezaee et al., 2023, Journal of Big Data) | RUS vs SMOTE with tree ensembles |
| [ ] | 31 | [A Deep Learning Ensemble With Data Resampling for Credit Card Fraud Detection](https://consensus.app/papers/details/6b119cb75517573e84ca3b9f69b72a8e/?utm_source=claude_desktop) (Mienye et al., 2023, IEEE Access) | SMOTE-ENN + LSTM/GRU |
| [ ] | 32 | [Hybrid Undersampling and Oversampling for Handling Imbalanced Credit Card Data](https://consensus.app/papers/details/b0a34f056a0857fead60f0b76c04653f/?utm_source=claude_desktop) (Alamri et al., 2024, IEEE Access) | Hybrid sampling |
| [ ] | 33 | [Performance Analysis of Cost-Sensitive Oversampling Mechanisms for Credit Card Fraud Detection](https://consensus.app/papers/details/3acc49db5e015571ad1773fc0f798c52/?utm_source=claude_desktop) (Ileberi et al., 2025, IEEE Access) | Cost-sensitive view (our future work) |

### D. Feature engineering

| Done | # | Paper | Note |
|---|---|---|---|
| [ ] | 34 | [An intelligent payment card fraud detection system](https://consensus.app/papers/details/fbbad3344e6f596382eeb25468ae14d4/?utm_source=claude_desktop) (Seera et al., 2021, Annals of Operations Research) | Aggregated features vs original, with hypothesis test |
| [ ] | 35 | [A Neural Network Ensemble With Feature Engineering for Improved Credit Card Fraud Detection](https://consensus.app/papers/details/cb638d9f87465caa913fe8c9d5292982/?utm_source=claude_desktop) (Esenogho et al., 2022, IEEE Access, 259 cit.) | Feature engineering + resampling |

### E. Temporal evaluation and concept drift

| Done | # | Paper | Note |
|---|---|---|---|
| [ ] | 36 | [Handling Concept Drift in Fraud Detection: A Replication Study](https://consensus.app/papers/details/e113f633066355e6b4d96257757c42ad/?utm_source=claude_desktop) (Topal et al., 2025, Canadian Conference on AI) | Finds simple methods can match complex ones |
| [ ] | 37 | [Beyond the Leaderboard: A Drift-Aware, Cost-Sensitive Evaluation Protocol for ML in Financial Fraud Detection](https://consensus.app/papers/details/87d8f96e600e501cb9a7f362ebafbd5e/?utm_source=claude_desktop) (Yerram, 2026) | Argues random splits inflate scores. Very close to our message, but a weaker venue: cite carefully |

### F. Data leakage and shortcut learning

| Done | # | Paper | Note |
|---|---|---|---|
| [ ] | 38 | [Don't push the button! Exploring data leakage risks in machine learning and transfer learning](https://consensus.app/papers/details/4496458033b654008576454fbc2ef354/?utm_source=claude_desktop) (Apicella et al., 2024, Artificial Intelligence Review) | Leakage taxonomy |
| [ ] | 39 | [Mitigating data bias and ensuring reliable evaluation of AI models with shortcut hull learning](https://consensus.app/papers/details/119b33f9d4cf51e48ff8c18da5884cc3/?utm_source=claude_desktop) (Zhou et al., 2025, Nature Communications) | Shortcut learning in datasets |
| [ ] | 40 | Shortcut learning in deep neural networks (Geirhos et al., 2020, Nature Machine Intelligence) | Already cited in our draft. Free version on arXiv: search "Geirhos shortcut learning arXiv" |

### G. Explainable AI

| Done | # | Paper | Note |
|---|---|---|---|
| [ ] | 41 | [Financial Fraud Detection Using Explainable AI and Stacking Ensemble Methods](https://consensus.app/papers/details/e131e0f96e07512faaa184dc215cf4bf/?utm_source=claude_desktop) (Almalki et al., 2025, arXiv) | SHAP, LIME, permutation importance |
| [ ] | 42 | [Secure and Transparent Banking: Explainable AI-Driven Federated Learning Model for Financial Fraud Detection](https://consensus.app/papers/details/35ea4afe49325677b980129f929b4551/?utm_source=claude_desktop) (Aljunaid et al., 2025, JRFM) | XAI in banking |

### H. Synthetic financial data

| Done | # | Paper | Note |
|---|---|---|---|
| [ ] | 43 | [Realistic Synthetic Financial Transactions for Anti-Money Laundering Models](https://consensus.app/papers/details/f5b9e5eb2fdd5a428b7cd13a2a0e99f6/?utm_source=claude_desktop) (Altman et al., 2023, arXiv/NeurIPS Datasets) | Agent-based generator, discusses limits of earlier simulators |
| [ ] | 44 | [Hide and seek in transaction networks: a multi-agent framework for simulating and detecting money laundering](https://consensus.app/papers/details/d59110c3a7275e1d938bd48cac72f778/?utm_source=claude_desktop) (Wang et al., 2025, Complex & Intelligent Systems) | Synthetic-to-real gap |

---

## Search strings (for Google Scholar, arXiv, IEEE Xplore, ScienceDirect, Semantic Scholar)

Copy-paste these. Tick "open access" / "free PDF" filters where available.

```
"PaySim" fraud detection
"PaySim" "machine learning" OR "deep learning"
"mobile money" fraud detection "machine learning"
"mobile financial services" fraud detection
"synthetic dataset" fraud detection evaluation
fraud detection "class imbalance" "precision-recall"
"feature engineering" transaction fraud detection
fraud detection "concept drift" "temporal split" OR "chronological"
"data leakage" machine learning evaluation
"shortcut learning" benchmark dataset bias
fraud detection "rule-based" versus "machine learning"
"explainable" fraud detection SHAP
```

Free-PDF sources: Google Scholar ("[PDF]" link on the right), arXiv, Semantic Scholar, MDPI, IEEE Access (fully open), Frontiers, PLoS ONE, Springer/Elsevier "open access" filter, ResearchGate (author uploads).
