import os
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details (with correct URL format)
engine = create_engine('postgresql://postgres:PKVvRUxD4p8uFVJPBQqR@predictivemaintenancedb.ctcu4ai6ckgn.us-east-1.rds.amazonaws.com:5432/postgres')

# Base directory containing CSV files
base_dir = 'dataSet'

# List of CSV file paths (using os.path.join for portability)
csv_files = [
    os.path.join(base_dir, 'experiment_01.csv'),
    os.path.join(base_dir, 'experiment_02.csv'),
    os.path.join(base_dir, 'experiment_03.csv'),
    os.path.join(base_dir, 'experiment_04.csv'),
    os.path.join(base_dir, 'experiment_05.csv'),
    os.path.join(base_dir, 'experiment_06.csv'),
    os.path.join(base_dir, 'experiment_07.csv'),
    os.path.join(base_dir, 'experiment_08.csv'),
    os.path.join(base_dir, 'experiment_09.csv'),
    os.path.join(base_dir, 'experiment_10.csv'),
    os.path.join(base_dir, 'experiment_11.csv'),
    os.path.join(base_dir, 'experiment_12.csv'),
    os.path.join(base_dir, 'experiment_13.csv'),
    os.path.join(base_dir, 'experiment_14.csv'),
    os.path.join(base_dir, 'experiment_15.csv'),
    os.path.join(base_dir, 'experiment_16.csv'),
    os.path.join(base_dir, 'experiment_17.csv'),
    os.path.join(base_dir, 'experiment_18.csv'),
]

# Loop through each CSV file
for csv_file in csv_files:
    try:
        # Extract the file name without extension for the table name
        table_name = os.path.splitext(os.path.basename(csv_file))[0]

        # Print the current file being processed
        print(f"Processing {csv_file} into table {table_name}...")

        # Load CSV data into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Create a new table in PostgreSQL for each CSV if it does not exist
        df.to_sql(table_name, engine, index=False, if_exists='replace')  # Use 'replace' to create a new table

        print(f"Successfully loaded {csv_file} into table {table_name}.")

    except Exception as e:
        # Print the error and the specific file causing it
        print(f"Error loading {csv_file}: {e}")