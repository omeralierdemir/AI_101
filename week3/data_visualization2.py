import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# CSV dosyasını oku
df = pd.read_csv("data/m_shape_3d_data.csv")

x = df["x"]
y = df["y"]
z = df["z"]

# 3D figür oluştur
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, linewidth=2)

ax.set_title("3D M Harfi İlk 3 Çizgi Görselleştirmesi")
ax.set_xlabel("X Ekseni")
ax.set_ylabel("Y Ekseni")
ax.set_zlabel("Z Ekseni")

# M harfi etkisi için Z ekseninden bak
ax.view_init(elev=10, azim=90)

plt.show()