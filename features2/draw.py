import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the .npy file
data = np.load("trainstruct3.npy")

# Ensure the data has three columns
if data.shape[1] != 3:
    raise ValueError("Expected a (N, 3) shaped array, but got {}".format(data.shape))

# Extract x, y, z coordinates
x, y, z = data[:, 0], data[:, 1], data[:, 2]

# Create a 3D scatter plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', marker='o')

# Labels and title
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Scatter Plot of trainstruct3.npy")

plt.show()
