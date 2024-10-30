import boto3
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

# Example results from your model evaluations
model_1_accuracy = 0.5
model_2_accuracy = 0.42

# Save results to a CSV file
results = {
    "Model": ["Model 1", "Model 2"],
    "Accuracy": [model_1_accuracy, model_2_accuracy]
}
results_df = pd.DataFrame(results)
results_df.to_csv('model_results.csv', index=False)

# Classification report for Model 2 as an example
model_2_report = classification_report([1, 0, 1, 1], [1, 1, 0, 1], output_dict=True)
report_df = pd.DataFrame(model_2_report).transpose()
report_df.to_csv('classification_report_model_2.csv', index=True)

# S3 setup: specify bucket name and the path in the bucket
bucket_name = 'predictive-results-bucket'
file_key_results = 'dataset/model_results.csv'  # Path where the file will be saved in S3
file_key_report = 'dataset/classification_report_model_2.csv'

# Initialize the S3 client
s3_client = boto3.client('s3')

# Upload files to S3
try:
    s3_client.upload_file('model_results.csv', bucket_name, file_key_results)
    print(f"Uploaded model_results.csv to s3://{bucket_name}/{file_key_results}")
    
    s3_client.upload_file('classification_report_model_2.csv', bucket_name, file_key_report)
    print(f"Uploaded classification_report_model_2.csv to s3://{bucket_name}/{file_key_report}")

except Exception as e:
    print("Error uploading to S3:", e)
