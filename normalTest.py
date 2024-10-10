import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Read data from an Excel file
file_path = 'KPWOI.xlsx'
sheet_name = 'Sheet2'

# Load the data from the specified sheet
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Transpose the DataFrame to swap rows and columns
data = data.T

# Ensure the correct column names (now rows)
time = data.iloc[0]  # row 1
level = data.iloc[1]  # row 2
square=data.iloc[2]
sqrt=data.iloc[3]

# Calculate the quantiles of the data
quantiles = np.percentile(sqrt, np.arange(0, 100, 1))

# Calculate the theoretical quantiles of a normal distribution
normal_quantiles = stats.norm.ppf(np.arange(0, 1, 0.01), loc=np.mean(sqrt), scale=np.std(sqrt))

# Calculate the quantile-to-quantile normal threshold (95% confidence interval)
threshold = np.abs(normal_quantiles - quantiles) / np.std(sqrt) * 1.96

# Create the Q-Q plot
plt.figure(figsize=(8, 6))
plt.scatter(normal_quantiles, quantiles)
plt.plot([min(normal_quantiles), max(normal_quantiles)], [min(normal_quantiles), max(normal_quantiles)], 'k--')

# Create the confidence intervals (threshold lines)
z = np.linspace(np.min(normal_quantiles), np.max(normal_quantiles), 100)
quantiles = np.percentile(sqrt, [25, 75])
q1, q3 = stats.norm.ppf([0.25, 0.75])
slope = (quantiles[1] - quantiles[0]) / (q3 - q1)
intercept = quantiles[0] - slope * q1

# Plot confidence interval lines
plt.plot(z, slope * z + intercept, color='brown', linewidth=2, label='Upper Threshold')  # Upper threshold
plt.plot(z, slope * z - intercept, color='brown', linewidth=2, label='Lower Threshold')  # Lower threshold

plt.xlabel('Theoretical Quantiles')
plt.ylabel('Observed Quantiles')
plt.title('Q-Q Plot of Level Data')
plt.legend()
plt.show()

print("Quantile-to-Quantile Normal Threshold (95% CI):")
print("Lower Threshold:", np.min(threshold))
print("Upper Threshold:", np.max(threshold))