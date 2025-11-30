import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ---------------------------------------------------------
# 1. Veri setini yükleme
# ---------------------------------------------------------
df = pd.read_csv("data/profesyonel_kan_veri_seti_small.csv")

print("Veri Seti Boyutu:", df.shape)
print(df.head())

# ---------------------------------------------------------
# 2. Eksik değer kontrolü
# ---------------------------------------------------------
print("\nEksik Değer Kontrolü:")
print(df.isnull().sum())

# ---------------------------------------------------------
# 3. Bağımsız ve bağımlı değişkenleri ayırma
# ---------------------------------------------------------
X = df.drop("Disease", axis=1)
y = df["Disease"]

# ---------------------------------------------------------
# 4. Eğitim/Test bölme
# ---------------------------------------------------------
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
# 6. KNN Modeli
# ---------------------------------------------------------
knn = KNeighborsClassifier(n_neighbors=3)  # k=5 ideal başlangıç noktasıdır
knn.fit(X_train_scaled, y_train)
# knn.fit(X_train, y_train) #No-Norm

# ---------------------------------------------------------
# 7. Tahmin ve Başarı Değerlendirme
# ---------------------------------------------------------
# y_pred = knn.predict(X_test) #No-Norm
y_pred = knn.predict(X_test_scaled)

print("\nDoğruluk Oranı:", accuracy_score(y_test, y_pred))
print("\nSınıflandırma Raporu:")
print(classification_report(y_test, y_pred))

print("\nKarmaşıklık Matrisi:")
print(confusion_matrix(y_test, y_pred))

# ---------------------------------------------------------
# 8. Yeni bir örnek tahmini
# ---------------------------------------------------------
# yeni_ornek = np.array([[
#     13,    # Hemoglobin
#     7,     # WBC
#     4.5,   # RBC
#     250,   # Platelet
#     110,   # Glucose
#     180,   # Cholesterol
#     90,    # Iron
#     30,    # Vitamin D
#     9.5,   # Calcium
#     4.2,   # Potassium
#     140,   # Sodium
#     1.0,   # Creatinine
#     0.5,   # Bilirubin
#     5,     # CRP
#     25,    # ALT
#     20     # AST
# ]])

# yeni_ornek_scaled = scaler.transform(yeni_ornek)
# tahmin = knn.predict(yeni_ornek_scaled)

# print("\nYeni örnek tahmini:", tahmin[0])