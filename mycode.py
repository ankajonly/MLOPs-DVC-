import pandas as pd 
import os

#Sample data
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

#Create DataFrame
df = pd.DataFrame(data)

#Create the data directory if it doesn't exist
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

#define the file path
file_path = os.path.join(data_dir, "people.csv")

#Save DataFrame to CSV
df.to_csv(file_path, index=False)

#print the file path
print(f"DataFrame saved to {file_path}")

