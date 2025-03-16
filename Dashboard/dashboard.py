# Import Libraries yang Diperlukan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set theme untuk Streamlit
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", page_icon="🚴", layout="wide")

# Menambahkan Judul dan Deskripsi
st.title("🚴 Dashboard Penyewaan Sepeda 🚴")
st.markdown(""" 
    **Dashboard Penyewaan Sepeda** yang menganalisis pengaruh cuaca, musim, waktu, hari kerja, 
    dan perbedaan antara pengguna kasual dan terdaftar terhadap jumlah penyewaan sepeda di sistem berbasis sepeda.
""")

# Memuat data yang sudah dibersihkan
hour_data = pd.read_csv('hour_data_cleaned.csv')  
day_data = pd.read_csv('day_data_cleaned.csv')    

# Menampilkan beberapa baris pertama dari dataset
st.write("### Data Penyewaan Sepeda (Hourly) - Sample Data:")
st.write(hour_data.head())

st.write("### Data Penyewaan Sepeda (Daily) - Sample Data:")
st.write(day_data.head())

# Visualisasi Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader('Pengaruh Cuaca terhadap Penyewaan Sepeda')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=hour_data, ax=ax, palette="coolwarm")
ax.set_title('Pengaruh Cuaca terhadap Penyewaan Sepeda')
ax.set_xlabel('Cuaca')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Visualisasi Pengaruh Musim terhadap Penyewaan Sepeda
st.subheader('Pengaruh Musim terhadap Penyewaan Sepeda')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=hour_data, ax=ax, palette="coolwarm")
ax.set_title('Pengaruh Musim terhadap Penyewaan Sepeda')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari
st.subheader('Pola Penyewaan Sepeda Berdasarkan Jam')
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hour_data, ax=ax, marker='o', color="dodgerblue")
ax.set_title('Pola Penyewaan Sepeda Berdasarkan Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Visualisasi Pengaruh Hari Kerja dan Libur terhadap Penyewaan Sepeda
st.subheader('Pengaruh Hari Kerja dan Libur terhadap Penyewaan Sepeda')

# Hari Kerja
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='workingday', y='cnt', data=hour_data, ax=ax, palette="viridis")
ax.set_title('Pengaruh Hari Kerja terhadap Penyewaan Sepeda')
ax.set_xlabel('Hari Kerja (0: Tidak, 1: Ya)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Hari Libur
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='holiday', y='cnt', data=hour_data, ax=ax, palette="viridis")
ax.set_title('Pengaruh Hari Libur terhadap Penyewaan Sepeda')
ax.set_xlabel('Hari Libur (0: Tidak, 1: Ya)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Perbedaan antara Pengguna Kasual dan Terdaftar
st.subheader('Perbedaan antara Pengguna Kasual dan Terdaftar')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='casual', y='cnt', data=hour_data, color='orange', label='Kasual', alpha=0.5, ax=ax)
sns.barplot(x='registered', y='cnt', data=hour_data, color='blue', label='Terdaftar', alpha=0.5, ax=ax)
ax.set_title('Perbandingan Penyewaan Sepeda antara Pengguna Kasual dan Terdaftar')
ax.set_xlabel('Pengguna')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.legend()
st.pyplot(fig)

# Menampilkan Total Penyewaan per Bulan dengan Fitur Interaktif
st.subheader("Jumlah Penyewaan Sepeda per Bulan")

# Menghitung Total Penyewaan per Bulan
monthly_rentals = hour_data.groupby('mnth')['cnt'].sum()

# Menambahkan Widget untuk Memilih Rentang Bulan
start_month, end_month = st.slider(
    "Pilih Rentang Bulan",
    min_value=1, max_value=12, value=(1, 12), step=1
)

# Filter data berdasarkan rentang bulan yang dipilih
filtered_monthly_rentals = monthly_rentals[start_month-1:end_month]

# Menampilkan Grafik dengan Rentang Bulan yang Dipilih
st.bar_chart(filtered_monthly_rentals)

# Menambahkan Footer dengan informasi Copyright
st.markdown(""" 
    --- 
    Data yang digunakan pada dashboard ini berasal dari [Bike Sharing Dataset](http://capitalbikeshare.com/system-data). 
    ### Dashboard Penyewaan Sepeda - 2025 
""")
