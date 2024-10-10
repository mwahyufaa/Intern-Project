import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from an Excel file
file_path = 'KPWOI.xlsx'
sheet_name = 'Sheet1'

# Load the data from the specified sheet
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Transpose the DataFrame to swap rows and columns
data = data.T

# Ensure the correct column names (now rows)
time = data.iloc[0]  # row 1
level = data.iloc[1]  # row 2
square=data.iloc[2]
sqrt=data.iloc[3]

# Calculate mean and standard deviation for the level row
mean_level = np.mean(level)
std_dev_level = np.std(level)

# Calculate z-scores
z_scores = np.abs((level - mean_level) / std_dev_level)

# Define thresholds
insignificant_threshold = 1
normal_threshold = 2
extreme_threshold = 3

# Find anomalies
insignificant_anomalies_level = level[z_scores >= insignificant_threshold]
normal_anomalies_level = level[(z_scores >= normal_threshold) & (z_scores < insignificant_threshold)]
extreme_anomalies_level = level[z_scores >= extreme_threshold]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, level, 'bo', label='Level Data')
plt.axhline(mean_level, color='blue', linestyle='--', label='Mean')

# Plot the threshold lines
plt.plot(time, [mean_level + std_dev_level] * len(time), color='green', linestyle='--', label='Insignificant Anomaly Threshold (Z=1)')
plt.plot(time, [mean_level + 2*std_dev_level] * len(time), color='yellow', linestyle='--', label='Moderate Anomaly Threshold (Z=2)')
plt.plot(time, [mean_level + 3*std_dev_level] * len(time), color='red', linestyle='--', label='Extreme Anomaly Threshold (Z=3)')
plt.plot(time, [mean_level - std_dev_level] * len(time), color='green', linestyle='--')
plt.plot(time, [mean_level - 2*std_dev_level] * len(time), color='yellow', linestyle='--')
plt.plot(time, [mean_level - 3*std_dev_level] * len(time), color='red', linestyle='--')

# Highlight anomalies
insig_time = time[z_scores >= insignificant_threshold]
insig_level = level[z_scores >= insignificant_threshold]

normal_time = time[(z_scores >= normal_threshold) & (z_scores < insignificant_threshold)]
normal_level = level[(z_scores >= normal_threshold) & (z_scores < insignificant_threshold)]

extreme_time = time[z_scores >= extreme_threshold]
extreme_level = level[z_scores >= extreme_threshold]

plt.plot(insig_time, insig_level, 'go', label='Insignificant Anomalies')
plt.plot(normal_time, normal_level, 'yo', label='Moderate Anomalies')
plt.plot(extreme_time, extreme_level, 'ro', label='Extreme Anomalies')

# Labels and title
plt.xlabel('Time')  # x-axis label
plt.ylabel('Level')  # y-axis label
plt.legend()
plt.show()

# Print anomalies
print("Insignificant Anomalies:", insignificant_anomalies_level)
print("Moderate Anomalies:", normal_anomalies_level)
print("Extreme Anomalies:", extreme_anomalies_level)