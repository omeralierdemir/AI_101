import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("data/housing_dataset.csv")

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df["square_meter"], df["year"], df["price"], s=25)

ax.set_xlabel("Metrekare")
ax.set_ylabel("Yıl")
ax.set_zlabel("Fiyat")
ax.set_title("3D Konut Fiyat Dağılımı")
plt.show()




"""
import pandas as pd
import matplotlib.pyplot as plt

df2 = pd.read_csv("data/dataset_2d.csv")

plt.figure(figsize=(10,5))
plt.plot(df2["x"], df2["y"], linewidth=2)

plt.title("2D Non-Linear Veri Seti")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dfA = pd.read_csv("data/dataset_3d_A.csv")

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection="3d")

ax.plot(dfA["x"], dfA["y"], dfA["z"], linewidth=2)

ax.set_title("3D Veri Seti A")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
"""