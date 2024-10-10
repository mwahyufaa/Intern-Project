import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from an Excel file
file_path = 'KPWOI.xlsx'
sheet_name = 'Sheet5'

# Load the data from the specified sheet
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Transpose the DataFrame to swap rows and columns
data = data.T

# Ensure the correct column names (now rows)
time = data.iloc[0]  # row 1
level = data.iloc[1]  # row 2

# Calculate mean and standard deviation for the square row
mean_square = np.mean(level)
std_dev_square = np.std(level)

# Calculate z-scores
z_scores_square = np.abs((level - mean_square) / std_dev_square)

# Find anomalies
insignificant_anomalies_square = level[z_scores_square >= 1]
moderate_anomalies_square = level[(z_scores_square >= 2) & (z_scores_square < 3)]
extreme_anomalies_square = level[z_scores_square >= 3]

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(level, z_scores_square, label='Square Data', color='blue')

# Plot thresholds
plt.axhline(y=1, color='green', linestyle='--', label='Insignificant Threshold')
plt.axhline(y=2, color='yellow', linestyle='--', label='Moderate Threshold')
plt.axhline(y=3, color='red', linestyle='--', label='Extreme Threshold')

# Highlight anomalies
plt.scatter(level[z_scores_square >= 1], z_scores_square[z_scores_square >= 1], label='Insignificant Anomalies', color='green')
plt.scatter(level[(z_scores_square >= 2) & (z_scores_square < 3)], z_scores_square[(z_scores_square >= 2) & (z_scores_square < 3)], label='Moderate Anomalies', color='yellow')
plt.scatter(level[z_scores_square >= 3], z_scores_square[z_scores_square >= 3], label='Extreme Anomalies', color='red')

plt.xlabel('Level (Scale 1-100)')
plt.ylabel('Z-Score')
plt.legend()
plt.show()