import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data
np.random.seed(0)
x = np.linspace(-5, 5, 50)
true_a = 2
true_b = -1
y = true_a * x + true_b + np.random.randn(len(x)) * 2  # noisy data

# Grid for a and b
A = np.linspace(-5, 5, 60)
B = np.linspace(-5, 5, 60)
A_grid, B_grid = np.meshgrid(A, B)

# Compute Absolute Error Cost Function
COST_grid = np.zeros_like(A_grid)

for i in range(len(A)):
    for j in range(len(B)):
        y_pred = A_grid[i, j] * x + B_grid[i, j]
        COST_grid[i, j] = np.sum(np.abs(y - y_pred))   # <-- L1 LOSS

# Plot 3D surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(A_grid, B_grid, COST_grid)

ax.set_xlabel("a")
ax.set_ylabel("b")
ax.set_zlabel("Cost (Absolute Error)")
ax.set_title("Absolute Error (L1 Loss) Cost Function for y = ax + b")

plt.show()
