# Bike Sharing Analytics Dashboard 🚲

Dashboard interaktif berbasis Streamlit untuk menganalisis pola penyewaan sepeda (Bike Sharing Dataset 2011–2012) berdasarkan jam sibuk, musim, kondisi cuaca, tren pertumbuhan bulanan, serta klasterisasi suhu.

## Struktur Folder
- `dashboard/` : Berisi script aplikasi Streamlit (`dashboard.py`) dan dataset bersih (`main_day_data.csv`, `main_hour_data.csv`).
- `data/` : Berisi dataset mentah (`day.csv`, `hour.csv`).
- `notebook.ipynb` : File Jupyter Notebook berisi proses lengkap Data Wrangling, EDA, Visualization, dan Advanced Analysis.
- `requirements.txt` : Daftar library Python yang dibutuhkan.

## Cara Menjalankan Dashboard Secara Lokal
1. Instal seluruh dependensi yang dibutuhkan:
   ```bash
   pip install -r requirements.txt