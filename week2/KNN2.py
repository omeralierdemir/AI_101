import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ---------------------------------------------------------
# 1. Veri setini yükleme
# ---------------------------------------------------------
df = pd.read_csv("data/profesyonel_kan_veri_seti_small.csv")
print("Veri Seti Boyutu:", df.shape)

# ---------------------------------------------------------
# 2. Sınıf dağılımını görselleştirme
# ---------------------------------------------------------
plt.figure(figsize=(10,5))
df["Disease"].value_counts().plot(kind="bar")
plt.title("Hastalık Sınıf Dağılımları")
plt.xlabel("Hastalık Sınıfı")
plt.ylabel("Adet")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 3. Özellik histogramları
# ---------------------------------------------------------
df.drop("Disease", axis=1).hist(figsize=(15,12), bins=20)
plt.suptitle("Kan Parametrelerinin Dağılımı", fontsize=16)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 4. Eğitim-test bölme
# ---------------------------------------------------------
X = df.drop("Disease", axis=1)
y = df["Disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# ---------------------------------------------------------
# 5. Normalizasyon
# ---------------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------------------------------------
# 6. KNN için en iyi K değerinin grafikle analizi
# ---------------------------------------------------------
k_values = range(1, 21)
acc_scores = []

for k in k_values:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train_scaled, y_train)
    y_pred_temp = knn_temp.predict(X_test_scaled)
    acc_scores.append(accuracy_score(y_test, y_pred_temp))

plt.figure(figsize=(10,5))
plt.plot(k_values, acc_scores, marker="o")
plt.title("K Değerine Göre KNN Doğruluk Oranı")
plt.xlabel("k")
plt.ylabel("Doğruluk")
plt.grid(True)
plt.show()

# ---------------------------------------------------------
# 7. En iyi k ile KNN eğitimi
# ---------------------------------------------------------
best_k = k_values[np.argmax(acc_scores)]
print("En iyi k:", best_k)

knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train_scaled, y_train)

# ---------------------------------------------------------
# 8. Sonuçlar
# ---------------------------------------------------------
y_pred = knn.predict(X_test_scaled)

print("\nDoğruluk Oranı:", accuracy_score(y_test, y_pred))
print("\nSınıflandırma Raporu:")
print(classification_report(y_test, y_pred))

print("\nKarmaşıklık Matrisi:")
print(confusion_matrix(y_test, y_pred))

# ---------------------------------------------------------
# 9. Yeni örnek tahmini
# ---------------------------------------------------------
# yeni_ornek = np.array([[
#     13,      # Hemoglobin
#     4.8,     # RBC
#     70,      # Iron
#     14,      # WBC (yüksek)
#     260,     # Platelet
#     110,     # Glucose
#     190,     # Cholesterol
#     32,      # VitaminD
#     9.4,     # Calcium
#     4.1,     # Potassium
#     140,     # Sodium
#     1.0,     # Creatinine
#     0.6,     # Bilirubin
#     55,      # CRP (çok yüksek → enfeksiyon)
#     30,      # ALT
#     25       # AST
# ]]) # large-data

yeni_ornek = np.array([[
    9.5,   # Hemoglobin
    3.6,   # RBC
    40     # Iron
]])

yeni_ornek_scaled = scaler.transform(yeni_ornek)
tahmin = knn.predict(yeni_ornek_scaled)

print("\nYeni örnek tahmini:", tahmin[0])