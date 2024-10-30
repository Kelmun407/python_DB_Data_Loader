import os
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

# Example results from your model evaluations
model_1_accuracy = 0.5
model_2_accuracy = 0.42

# Define the path for the dataSet folder within the project directory
output_folder = 'dataSet'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# File paths within the dataSet folder
file_path_results = os.path.join(output_folder, 'model_results.csv')
file_path_report = os.path.join(output_folder, 'classification_report_model_2.csv')

# Save model results to CSV
results = {
    "Model": ["Model 1", "Model 2"],
    "Accuracy": [model_1_accuracy, model_2_accuracy]
}
results_df = pd.DataFrame(results)
results_df.to_csv(file_path_results, index=False)
print(f"Model results saved to {file_path_results}")

# Save classification report for Model 2
model_2_report = classification_report([1, 0, 1, 1], [1, 1, 0, 1], output_dict=True)
report_df = pd.DataFrame(model_2_report).transpose()
report_df.to_csv(file_path_report, index=True)
print(f"Classification report saved to {file_path_report}")
