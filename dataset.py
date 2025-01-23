import pandas as pd
import random

# Parameters for the dataset
num_samples = 100
output_file = "manufacturing_data.csv"

# Generate synthetic data
data = {
    "Machine_ID": [f"M{random.randint(1, 50)}" for _ in range(num_samples)],
    "Temperature": [random.uniform(50, 120) for _ in range(num_samples)],
    "Run_Time": [random.uniform(100, 1000) for _ in range(num_samples)],
    "Downtime_Flag": [random.choice([0, 1]) for _ in range(num_samples)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv(output_file, index=False)
print(f"Synthetic dataset generated: {'C:\Users\ekshi\OneDrive\Desktop\project\manufacturing_data.csv>'})
