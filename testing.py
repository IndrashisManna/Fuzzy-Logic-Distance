import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data from the CSV file
file1_path = r'G:\Python code\Fuzzy logic\file1 - Copy.csv'
data = pd.read_csv(file1_path)

# Extract the first 3 columns
col1 = data['mean']
col2 = data['std dis']
col3 = data['percent']

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data points
ax.scatter(col1, col2, col3, c='blue', marker='o')

# Set labels and title
ax.set_xlabel('Mean')
ax.set_ylabel('Standard Deviation')
ax.set_zlabel('Percent')
ax.set_title('3D Plot of Mean, Standard Deviation, and Percent')

# Show the plot
plt.show()
