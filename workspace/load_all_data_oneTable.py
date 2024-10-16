import os
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details 
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

# Database table name where the data will be inserted
table_name = 'experiments_data'

# Loop through each CSV file
for csv_file in csv_files:
    try:
        # Print the current file being processed
        print(f"Processing {csv_file}...")
        
        # Load CSV data into a pandas DataFrame in chunks 
        chunk_size = 10000  # Adjust the chunk size based on your data
        for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
            # Insert the data into PostgreSQL table
            chunk.to_sql(table_name, engine, index=False, if_exists='append')
        
        print(f"Successfully loaded {csv_file} into {table_name}.")

    except Exception as e:
    
        print(f"Error loading {csv_file}: {e}")
