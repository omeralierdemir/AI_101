import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Veri setlerini yükle
df2 = pd.read_csv("data/2ozellikli_3sinif.csv")
df3 = pd.read_csv("data/3ozellikli_3sinif.csv")

# ---------------------------------------------------------
# 1) 2 Özellikli Veri Seti – 2D Scatter Plot
# ---------------------------------------------------------
plt.figure(figsize=(7,6))

for label in df2["Label"].unique():
    subset = df2[df2["Label"] == label]
    plt.scatter(subset["F1"], subset["F2"], label=f"Sınıf {label}")

plt.title("2 Özellikli Veri Seti (3 Sınıf)")
plt.xlabel("F1")
plt.ylabel("F2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 2) 3 Özellikli Veri Seti – 3D Scatter Plot
# ---------------------------------------------------------
fig = plt.figure(figsize=(8,7))
ax = fig.add_subplot(111, projection='3d')

for label in df3["Label"].unique():
    subset = df3[df3["Label"] == label]
    ax.scatter(subset["F1"], subset["F2"], subset["F3"], label=f"Sınıf {label}")

ax.set_title("3 Özellikli Veri Seti (3 Sınıf)")
ax.set_xlabel("F1")
ax.set_ylabel("F2")
ax.set_zlabel("F3")
ax.legend()

plt.show()