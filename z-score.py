import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from an Excel file
file_path = 'data/data.xlsx'
sheet_name = 'plot-data-1'

# Load the data from the specified sheet
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Transpose the DataFrame to swap rows and columns
data = data.T

# Ensure the correct column names (now rows)
time = data.iloc[0]  # row 1
level = data.iloc[1]  # row 2
square=data.iloc[2]
sqrt=data.iloc[3]

# Calculate the mean and standard deviation of the level data
mean_level = np.mean(level)
std_dev_level = np.std(level)

# Calculate the z-score for the level data
z_score_level = (level - mean_level) / std_dev_level

# Print the z-scores
print("Z-scores for level data:")
print(z_score_level)

# You can also calculate the z-score for other data (e.g., square, sqrt) in a similar way
mean_square = np.mean(square)
std_dev_square = np.std(square)
z_score_square = (square - mean_square) / std_dev_square

mean_sqrt = np.mean(sqrt)
std_dev_sqrt = np.std(sqrt)
z_score_sqrt = (sqrt - mean_sqrt) / std_dev_sqrt

print("\nZ-scores for square data:")
print(z_score_square)

print("\nZ-scores for sqrt data:")
print(z_score_sqrt)