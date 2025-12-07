import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data
np.random.seed(0)
x = np.linspace(-5, 5, 50)
true_a = 2
true_b = -1
y = true_a * x + true_b + np.random.randn(len(x)) * 2  # noisy line

# Grid for a and b
A = np.linspace(-5, 5, 50)
B = np.linspace(-5, 5, 50)
A_grid, B_grid = np.meshgrid(A, B)

# Compute MSE for each (a, b)
MSE_grid = np.zeros_like(A_grid)
for i in range(len(A)):
    for j in range(len(B)):
        y_pred = A_grid[i, j] * x + B_grid[i, j]
        MSE_grid[i, j] = np.mean((y - y_pred)**2)

# Plot 3D surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(A_grid, B_grid, MSE_grid)

ax.set_xlabel("a")
ax.set_ylabel("b")
ax.set_zlabel("MSE")
ax.set_title("MSE Surface for y = ax + b")

plt.show()
