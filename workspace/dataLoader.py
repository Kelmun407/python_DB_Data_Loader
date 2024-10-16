import os
import pandas as pd
from sqlalchemy import create_engine # pip install sqlalchemy


# Connect to PostgreSQL
engine = create_engine('postgres://postgres:PKVvRUxD4p8uFVJPBQqR@predictivemaintenancedb.ctcu4ai6ckgn.us-east-1.rds.amazonaws.com:5432/postgres')

# List of CSV file paths 
csv_files = [
    'dataSet\experiment_01.csv',
    'dataSet\experiment_02.csv',
    'dataSet\experiment_03.csv',
    'dataSet\experiment_04.csv',
    'dataSet\experiment_05.csv',
    'dataSet\experiment_06.csv',
    'dataSet\experiment_07.csv',
    'dataSet\experiment_08.csv',
    'dataSet\experiment_09.csv',
    'dataSet\experiment_10.csv',
    'dataSet\experiment_11.csv',
    'dataSet\experiment_12.csv',
    'dataSet\experiment_13.csv',
    'dataSet\experiment_14.csv',
    'dataSet\experiment_15.csv',
    'dataSet\experiment_16.csv',
    'dataSet\experiment_17.csv',
    'dataSet\experiment_18.csv',
]

# Database table name where the data will be inserted
table_name = 'your_table_name'

# Loop through each CSV file
for csv_file in csv_files:
    try:
        # Load CSV data into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Print status
        print(f"Loading data from {csv_file} into {table_name}...")

        # Insert the data into PostgreSQL table
        df.to_sql(table_name, engine, index=False, if_exists='append')

        # Print success message
        print(f"Successfully loaded {csv_file} into {table_name}.")

    except Exception as e:
        print(f"Error loading {csv_file}: {e}")
