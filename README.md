# Bike Sharing Analytics Dashboard 

Dashboard interaktif berbasis Streamlit untuk menganalisis pola penyewaan sepeda (*Bike Sharing Dataset* 2011–2012) berdasarkan jam sibuk, musim, kondisi cuaca, tren pertumbuhan bulanan, serta klasterisasi suhu.

## Struktur Folder
- `dashboard/` : Berisi script aplikasi Streamlit (`dashboard.py`) dan dataset bersih (`main_day_data.csv`, `main_hour_data.csv`).
- `data/` : Berisi dataset mentah (`day.csv`, `hour.csv`).
- `notebook.ipynb` : File Jupyter Notebook berisi proses lengkap *Data Wrangling*, *EDA*, *Visualization*, dan *Advanced Analysis*.
- `requirements.txt` : Daftar library Python yang dibutuhkan.
- `url.txt` : Tautan publik dashboard yang telah di-*deploy* di Streamlit Community Cloud.

## Setup Environment - Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```bash
python -m venv venv
# Aktivasi di Windows:
venv\Scripts\activate
# Aktivasi di Mac/Linux:
# source venv/bin/activate

pip install -r requirements.txt
```

## Run Streamlit App
```bash
streamlit run dashboard/dashboard.py
```
