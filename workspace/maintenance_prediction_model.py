import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
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

# Train-test split without stratification
X_train_split_1, X_test_split_1, y_train_split_1, y_test_split_1 = train_test_split(
    X_train_1, y_train_1, test_size=0.2, random_state=42
)

# Train Model 1 on train.csv
model_1 = RandomForestClassifier(n_estimators=50, random_state=42)
model_1.fit(X_train_split_1, y_train_split_1)

# Evaluate Model 1 on train.csv test split
predictions_1 = model_1.predict(X_test_split_1)
print("Model 1 - Accuracy on train.csv test split:", accuracy_score(y_test_split_1, predictions_1))
print(classification_report(y_test_split_1, predictions_1))

### Model 2: Train and Evaluate on experiments_data.csv ###

# Load experiments_data.csv data
experiment_df = pd.read_sql("SELECT * FROM experiments_data", engine)

# Define features and target for Model 2 (using available columns)
X_train_2 = experiment_df[['X1_ActualPosition', 'X1_ActualVelocity', 'X1_CurrentFeedback', 
                           'Y1_ActualPosition', 'Y1_ActualVelocity', 'Y1_CurrentFeedback',
                           'Z1_ActualPosition', 'Z1_ActualVelocity', 'Z1_CurrentFeedback']]
y_train_2 = experiment_df['Machining_Process']  # Ensure this column is suitable as the target

# Train-test split without stratification
X_train_split_2, X_test_split_2, y_train_split_2, y_test_split_2 = train_test_split(
    X_train_2, y_train_2, test_size=0.2, random_state=42
)

# Train Model 2 on experiments_data.csv
model_2 = RandomForestClassifier(n_estimators=50, random_state=42)
model_2.fit(X_train_split_2, y_train_split_2)

# Evaluate Model 2 on experiments_data.csv test split
predictions_2 = model_2.predict(X_test_split_2)
print("Model 2 - Accuracy on experiments_data.csv test split:", accuracy_score(y_test_split_2, predictions_2))
print(classification_report(y_test_split_2, predictions_2))
