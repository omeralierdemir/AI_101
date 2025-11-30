# 🚀 Proje Kurulum Rehberi

Bu doküman; Python kurulumu, VSCode veya PyCharm IDE'lerinin yüklenmesi, sanal ortam oluşturulması ve `requirements.txt` dosyasının kurulumu için gerekli tüm adımları tek bir yerde toplar.  
Hazırsan hemen başlayalım! ⚡

---

## 🐍 1. Python Kurulumu

### 📥 Python İndir
Resmi siteden son sürümü indir:

👉 https://www.python.org/downloads/

Kurulum sırasında mutlaka:
- **Add Python to PATH** kutusunu işaretle.

### 🔍 Kurulumu Doğrula
Terminal (CMD / PowerShell) aç ve:

```bash
python --version
```

Bir sürüm çıkıyorsa Python başarıyla kuruldu.

---

## 🖥️ 2. IDE Kurulumu

### ✨ Seçenek 1 — Visual Studio Code (VSCode)

📥 VSCode indir:  
👉 https://code.visualstudio.com/

#### 🔌 Gerekli Eklentiler
VSCode aç → Extensions (`CTRL + SHIFT + X`):

- Python (Microsoft)
- Pylance
- (İsteğe bağlı) Jupyter, Code Runner

---

### ✨ Seçenek 2 — PyCharm

📥 PyCharm indir:  
👉 https://www.jetbrains.com/pycharm/download/

- **Community Edition** ücretsizdir.
- Python projeleri için otomatik yapılandırma sağlar.

---

## 📂 3. Projeyi Hazırlama

Proje klasörüne gir:

```bash
cd proje_klasorun
```

---

## 🌱 4. Sanal Ortam (Virtual Environment) Oluşturma

#### 💡 Önerilir: Her proje için ayrı ortam

### Sanal Ortam Oluştur
```bash
python -m venv venv
```

### Sanal Ortamı Aktifleştir

#### Windows:
```bash
venv\Scripts\activate
```

#### Mac / Linux:
```bash
source venv/bin/activate
```

Aktif olduğunda terminal başında `(venv)` görünür.

---

## 📦 5. requirements.txt Kurulumu

Aşağıdaki komutla bağımlılıkları yükle:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Bu komutlar projedeki tüm paketleri tek seferde kurar.

---

## ▶️ 6. Projeyi Çalıştırma

Örneğin ana dosya `main.py` ise:

```bash
python main.py
```

---

## 🧪 7. Örnek Proje Klasör Yapısı

```
project/
│── venv/
│── week1/
│   └── algorithm_name.py
│── data/
│── requirements.txt
│── readme.md
│──syllabus.md
```

---

## 🔧 8. Sorun Giderme (Troubleshooting)

### ❗ pip çalışmıyor
Python PATH’e eklenmemiş olabilir → Python’u yeniden kur ve PATH kutusunu işaretle.

### ❗ VSCode doğru Python’ı görmüyor
```
CTRL + SHIFT + P
```
"Python: Select Interpreter" → **venv** seç.

### ❗ Bağımlılık hatası
```bash
pip install -r requirements.txt
```

### ❗ PyCharm yanlış interpreter seçmiş
Settings → Project Interpreter → **venv/bin/python** seç.

---

## 🎉 Hepsi Bu Kadar!

Artık Python kurulumu, IDE ayarları, sanal ortam ve bağımlılık yönetimi tamamen hazır.  
Projeni ışık hızında geliştirebilirsin! 🚀🔥