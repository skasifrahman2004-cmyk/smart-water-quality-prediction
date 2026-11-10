# Smart Water Quality Prediction

This repository contains a machine learning project to predict water potability based on physicochemical water quality metrics.

## Dataset
The dataset used is the Kaggle Water Potability dataset consisting of 3,276 water samples with 9 features:
- pH value
- Hardness
- Solids (Total Dissolved Solids)
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity
- Potability (Target: 0 = Non-Potable, 1 = Potable)

## Pipeline Overview
1. Data Cleaning: Handled missing values using median imputation for features with null entries.
2. Feature Scaling: Normalized feature values using StandardScaler.
3. Model Training & Comparison: Evaluated Logistic Regression, Random Forest, and Gradient Boosting.
4. Validation: Evaluated using 5-fold cross-validation and confusion matrix analysis.
5. Web App: Created an interactive testing interface using Streamlit.

## Results
- Logistic Regression: Accuracy = 60.98%, ROC-AUC = 54.81%
- Gradient Boosting: Accuracy = 65.24%, ROC-AUC = 62.88%
- Random Forest: Accuracy = 65.85%, ROC-AUC = 64.07% (Mean 5-fold CV Accuracy: 66.68%)

Random Forest was selected as the final model and saved as `water_quality_model.pkl`.

## How to Run
1. Install requirements:
   pip install -r requirements.txt

2. Run the Streamlit app:
   streamlit run app.py