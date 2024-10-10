import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('levelhmi.csv', index_col='Time')

# Define the threshold values
threshold_low = 40  # percentage
threshold_high = 50 # percentage

# Define a function to detect anomalies
def detect_anomalies(df, threshold_low, threshold_high):
    # Create a new column to store the anomaly status
    df['anomaly'] = 0
    
    # Iterate over the rows
    for index, row in df.iterrows():
        # Check if the percentage value is outside the threshold range
        if row['Level'] < threshold_low or row['Level'] > threshold_high:
            # Mark the row as an anomaly
            df.loc[index, 'anomaly'] = 1
    
    return df

# Apply the anomaly detection function
df_anomalies = detect_anomalies(df, threshold_low, threshold_high)

# Print plot
plt.figure(figsize=(10,6))
plt.plot(df_anomalies.index, df_anomalies['Level'], label='Percentage')
plt.axhline(y=threshold_low, color='red', linestyle='--', label='Threshold Low')
plt.axhline(y=threshold_high, color='red', linestyle='--', label='Threshold High')
plt.scatter(df_anomalies.index[df_anomalies['anomaly'] == 1], df_anomalies['Level'][df_anomalies['anomaly'] == 1], color='red', label='Anomalies')
plt.xlabel('Time Duration (Hours)')
plt.ylabel('Level Percentage (%)')
plt.title('Anomaly Detection')
plt.legend()
plt.show()