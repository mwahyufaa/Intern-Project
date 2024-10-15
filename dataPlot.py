import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

# Plotting the impulse graph
plt.figure()
plt.stem(time, level)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Level')

# Customize x-axis
plt.xlim(0, 150)  # set x-axis min and max values
majorLocator = ticker.MultipleLocator(24)  # major ticks every 24 units
minorLocator = ticker.MultipleLocator(12)  # minor ticks every 12 units
plt.gca().xaxis.set_major_locator(majorLocator)
plt.gca().xaxis.set_minor_locator(minorLocator)

plt.ylim(0, 100)  # set x-axis min and max values
majorLocator = ticker.MultipleLocator(10)  # major ticks every 24 units
minorLocator = ticker.MultipleLocator(5)  # minor ticks every 12 units
plt.gca().yaxis.set_major_locator(majorLocator)
plt.gca().yaxis.set_minor_locator(minorLocator)

# Show the plot
plt.show()