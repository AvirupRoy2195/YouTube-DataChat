import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("shaistashahid/youtube-analytics-data")

print("Path to dataset files:", path)

# Find the CSV file
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
if csv_files:
    csv_path = os.path.join(path, csv_files[0])
    print(f"Reading file: {csv_path}")
    df = pd.read_csv(csv_path)
    print(df.head(10))
else:
    print("No CSV file found in the dataset.")
