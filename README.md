# Breast Cancer Classification using SVC and GridSearchCV

A machine learning project that classifies breast tumors as **benign** or **malignant** using a Support Vector Classifier (SVC), with hyperparameters tuned using GridSearchCV and 5-fold cross-validation.

Built as our B.Tech final-year major project (CSE – AI & ML, Guru Nanak Institutions, 2025–26) in a team of three.

> **Disclaimer:** This is an academic project. It is not a medical tool and must not be used for diagnosis or clinical decisions.

---

## Results

Evaluated on a held-out test set (20% of the data, 114 samples):

| Metric    | Score  |
|-----------|--------|
| Accuracy  | ~98.2% |
| Precision | 100%   |
| Recall    | ~95.3% |
| F1-score  | ~97.6% |

- **Best hyperparameters:** `kernel='rbf'`, `C=10`, `gamma='auto'`
- **Mean 5-fold cross-validation accuracy (training data):** ~94.7%


## Dataset

[Wisconsin Breast Cancer Diagnostic (WBCD)](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset): 569 samples (357 benign, 212 malignant).

Nine of the "mean" features are used:

`radius_mean`, `texture_mean`, `perimeter_mean`, `area_mean`, `smoothness_mean`, `concavity_mean`, `concave points_mean`, `symmetry_mean`, `fractal_dimension_mean`

---

## Approach

1. Load the dataset and select the 9 features
2. Encode the target (`B` → 0, `M` → 1)
3. Exploratory analysis: box plot, histogram, and scatter plot of radius vs. texture by diagnosis
4. Standardize features with `StandardScaler`
5. 80/20 train–test split (`random_state=42`)
6. Train an `SVC` and tune it with `GridSearchCV` (5-fold CV) over:
   - `C`: 0.1, 1, 10
   - `kernel`: linear, rbf
   - `gamma`: scale, auto
7. Evaluate on the test set (accuracy, precision, recall, F1)
8. Save the best model with `pickle`

---


### Screenshots

| Input form | Result page | Performance |
|------------|-------------|-------------|
|<img width="795" height="381" alt="image" src="https://github.com/user-attachments/assets/fd3d018a-36e0-4563-a8c0-23ef68ba91d6" /> | <img width="795" height="346" alt="image" src="https://github.com/user-attachments/assets/50d9c892-4f04-4009-9e49-881ae73d7f81" />  <img width="722" height="295" alt="image" src="https://github.com/user-attachments/assets/e27d4c21-3db4-4a31-8107-42d2ce9cf4d0" />
|<img width="722" height="362" alt="image" src="https://github.com/user-attachments/assets/815528f9-ab9d-47d5-b6c5-84e3a6dd8b06" />
|

---

## Project structure

```
.
├── PROJ_2.ipynb                 # Data prep, EDA, training, tuning, evaluation
├── data.csv                     # WBCD dataset
├── SVM_model1.pkl               # Trained SVC (best estimator from GridSearchCV)
├── scaler.pkl                   # Fitted StandardScaler used by the web app
├── app.py                       # Flask web app
├── requirements.txt
├── Final Document(Major Project)-FINAL.pdf   # Project report
└── screenshots/
```


## How to run

**Notebook (model training)**

```bash
git clone https://github.com/Aditya-hub31/Improving-Breast-Cancer-Classification-Using-SVC-GridSearchCV.git
cd Improving-Breast-Cancer-Classification-Using-SVC-GridSearchCV
pip install -r requirements.txt
jupyter notebook PROJ_2.ipynb
```

**Web app**

```bash
python app.py
# open http://127.0.0.1:5000
```

---

## Tech stack

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · Flask · HTML/CSS · Jupyter Notebook

---

## Known limitations

- Single dataset, single train/test split. Results on other datasets or splits may differ.
- Only an SVC was tuned. The notebook does not compare it against other models.
- In the notebook, the scaler is fit on the full dataset before the split, which leaks a little test-set information. A cleaner version would fit it on the training data only (or use a scikit-learn `Pipeline`).
- The web app is a demo: users are stored in memory with plain-text passwords, and it is not meant for deployment.

## Possible improvements

- Use a `Pipeline` for scaling and training to remove the leakage above
- Compare against Logistic Regression, Random Forest, and Gradient Boosting
- Report a confusion matrix and ROC-AUC
- Deploy a simple demo app (for example with Streamlit)

---


## Contact

Aditya Karnati · [LinkedIn](https://www.linkedin.com/in/aditya-karnati) · [GitHub](https://github.com/Aditya-hub31)
