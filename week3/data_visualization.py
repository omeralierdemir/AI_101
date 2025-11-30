import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv("data/diagonal_with_bias.csv")

# Görselleştir
plt.figure(figsize=(7, 5))
plt.scatter(df["x"], df["y"])
plt.title("Bias Eklenmiş Çapraz Veri")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
