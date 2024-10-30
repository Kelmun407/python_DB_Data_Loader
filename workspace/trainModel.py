import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Connect to PostgreSQL and load data
engine = create_engine('postgresql://postgres:PKVvRUxD4p8uFVJPBQqR@predictivemaintenancedb.ctcu4ai6ckgn.us-east-1.rds.amazonaws.com:5432/postgres')

### Model 1: Train and Evaluate on train.csv ###

# Load train.csv data
train_df = pd.read_sql("SELECT * FROM train", engine)

# Define features and target for Model 1
X_train_1 = train_df[['feedrate', 'clamp_pressure']]
y_train_1 = train_df['tool_condition'].apply(lambda x: 1 if x == 'worn' else 0)

# Train-test split for Model 1
X_train_split_1, X_test_split_1, y_train_split_1, y_test_split_1 = train_test_split(
    X_train_1, y_train_1, test_size=0.2, random_state=42, stratify=y_train_1
)

# Train Model 1 on train.csv
model_1 = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=5, class_weight='balanced', random_state=42)
model_1.fit(X_train_split_1, y_train_split_1)

# Evaluate Model 1 on train.csv test split
predictions_1 = model_1.predict(X_test_split_1)
print("Model 1 - Accuracy on train.csv test split:", accuracy_score(y_test_split_1, predictions_1))
print(classification_report(y_test_split_1, predictions_1))

# Cross-validation for Model 1
cv_scores_1 = cross_val_score(model_1, X_train_1, y_train_1, cv=5)
print("Model 1 - Cross-validation accuracy:", cv_scores_1.mean())

### Model 2: Train and Evaluate on experiments_data.csv ###

# Load experiments_data.csv data
experiment_df = pd.read_sql("SELECT * FROM experiments_data", engine)

# Print available columns in experiments_data.csv to verify feature selection
print("Columns in experiments_data.csv:", experiment_df.columns.tolist())

# Define possible features for Model 2
possible_features_2 = [
    'X1_ActualPosition', 'X1_ActualVelocity', 'X1_ActualAcceleration', 
    'Y1_ActualPosition', 'Y1_ActualVelocity', 'Y1_ActualAcceleration',
    'Z1_ActualPosition', 'Z1_ActualVelocity', 'Z1_ActualAcceleration',
    'X1_CurrentFeedback', 'X1_DCBusVoltage', 'X1_OutputCurrent',
    'Y1_CurrentFeedback', 'Y1_DCBusVoltage', 'Y1_OutputCurrent',
    'Z1_CurrentFeedback', 'Z1_DCBusVoltage', 'Z1_OutputCurrent',
    'X1_OutputPower', 'Y1_OutputPower', 'Z1_OutputPower'
]

# Select only the features that are present in experiments_data.csv
X_train_2 = experiment_df[[col for col in possible_features_2 if col in experiment_df.columns]]

# Assuming 'Machining_Process' or another column is the target in experiments_data.csv
y_train_2 = experiment_df['Machining_Process']  # Replace with the actual target column if different

# Train-test split for Model 2
X_train_split_2, X_test_split_2, y_train_split_2, y_test_split_2 = train_test_split(
    X_train_2, y_train_2, test_size=0.2, random_state=42, stratify=y_train_2
)

# Train Model 2 on experiments_data.csv
model_2 = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=5, class_weight='balanced', random_state=42)
model_2.fit(X_train_split_2, y_train_split_2)

# Evaluate Model 2 on experiments_data.csv test split
predictions_2 = model_2.predict(X_test_split_2)
print("Model 2 - Accuracy on experiments_data.csv test split:", accuracy_score(y_test_split_2, predictions_2))
print(classification_report(y_test_split_2, predictions_2))

# Cross-validation for Model 2
cv_scores_2 = cross_val_score(model_2, X_train_2, y_train_2, cv=5)
print("Model 2 - Cross-validation accuracy:", cv_scores_2.mean())
