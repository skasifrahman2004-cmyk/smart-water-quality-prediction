# Smart Water Quality Prediction & Potability Classifier

### Student Details
- **Name:** Sk Asif Rahman
- **College:** Ghani Khan Choudhury Institute of Engineering and Technology (MAKAUT)
- **Department:** CSE (AI & ML)

Smart Water Quality Prediction & Potability Classifier is a machine learning project built to classify whether drinking water samples are potable or non-potable from chemical and physical measurements. It preprocesses sensor data, compares three classical machine-learning models, saves the best-performing model and scaler, and provides an interactive Streamlit web app for real-time prediction.

## Dataset
The dataset used is the Kaggle Water Potability dataset consisting of **3,276** water samples with **9** physicochemical features:
- pH value
- Hardness
- Solids (Total Dissolved Solids)
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity
- **Potability** (Target: `0` = Non-Potable, `1` = Potable)

## Pipeline Overview
1. **Data Cleaning:** Handled missing values using median imputation for features with null entries.
2. **Feature Scaling:** Normalized feature values using `StandardScaler`.
3. **Model Training & Comparison:** Evaluated Logistic Regression, Gradient Boosting, and Random Forest.
4. **Validation:** Evaluated using Stratified 5-Fold Cross-Validation, ROC-AUC, and confusion matrix analysis.
5. **Web App:** Created an interactive testing interface using Streamlit.

## Results
- **Logistic Regression:** Accuracy = `60.98%`, ROC-AUC = `54.81%`
- **Gradient Boosting:** Accuracy = `65.24%`, ROC-AUC = `62.88%`
- **Random Forest:** Accuracy = `65.85%`, ROC-AUC = `64.07%` (Mean 5-fold CV Accuracy: `66.68%`)

Random Forest was selected as the final model and saved as `water_quality_model.pkl` alongside `scaler.pkl`.

## Limitations
- Missing sensor readings (~15% in Sulfate), class imbalance (~61% non-potable vs. ~39% potable), and noisy measurements make this an academic prototype rather than a substitute for clinical water testing.

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run the Streamlit app: `streamlit run app.py`
