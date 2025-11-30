import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# Veri yükle
df = pd.read_csv("data/ev_fiyatlari.csv")

plt.figure(figsize=(7, 5))
plt.scatter(df["metrekare"], df["fiyat"])
plt.title("Ev Fiyatlari")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# Model için reshape
X = df[["metrekare"]]   # bağımsız değişken
y = df["fiyat"]         # bağımlı değişken

# Model oluştur
model = LinearRegression()
model.fit(X, y)

print("Eğim (m2 fiyatı):", model.coef_[0])
print("Bias (sabit):", model.intercept_)

x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line = model.predict(x_line)

# --- Görselleştir ---
plt.figure(figsize=(8, 5))
plt.scatter(X, y, label="Veri Noktaları")
plt.plot(x_line, y_line, linewidth=2, color="purple", label="Regresyon Doğrusu")
plt.xlabel("Metrekare")
plt.ylabel("Fiyat")
plt.title("Linear Regression – Öğrenilen Doğru")
plt.legend()
plt.grid(True)
plt.show()


# Örnek input ile tahmin yapma
while True:
    try:
        user_m2 = float(input("Metrekare girin (çıkmak için -1): "))
        if user_m2 == -1:
            break

        tahmin = model.predict([[user_m2]])
        print(f"{user_m2} m² bir evin tahmini fiyatı: {int(tahmin[0])} TL\n")
    except:
        print("Geçerli bir sayı giriniz.\n")
