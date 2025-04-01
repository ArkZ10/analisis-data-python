import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Proyek Analisis Data: Bike Sharing Dataset :sparkles:")
# st.markdown("- **Nama:** Annisa Saninah")
# st.markdown("- **Email:** saninahannisa@gmail.com") 
# st.markdown("- **ID Dicoding:** annisa1212") 
    
# Membaca data
all_df = pd.read_csv("dashboard/all_data.csv")
all_df["dteday"] = pd.to_datetime(all_df["dteday"], errors='coerce')

# Mengelompokkan data berdasarkan musim dan menghitung jumlah peminjaman sepeda
season_rentals = all_df.groupby("season")["cnt_day"].sum().sort_values(ascending=False)

# Mengelompokkan data berdasarkan jam dan menghitung jumlah peminjaman sepeda
hourly_rentals = all_df.groupby("hr")["cnt_hour"].sum()

# Mengelompokkan data berdasarkan kondisi cuaca dan menghitung jumlah peminjaman sepeda
weather_rentals = all_df.groupby("weathersit_day")["cnt_day"].sum().sort_values(ascending=False)

with st.sidebar:
    st.title("Proyek Nisa")
    st.image("logo.png")
    st.title("Filter")

# Pastikan kolom tanggal tidak ada nilai NaN
all_df = all_df.dropna(subset=["dteday"])

min_date = all_df["dteday"].min().date()
max_date = all_df["dteday"].max().date()

start_date = st.sidebar.date_input("Tanggal Mulai", min_date)
end_date = st.sidebar.date_input("Tanggal Akhir", max_date)

# Convert 'dteday' to datetime if it isn't already
all_df['dteday'] = pd.to_datetime(all_df['dteday'], errors='coerce')

# Filter data based on the selected date range
filtered_df = all_df[
    (all_df['dteday'] >= pd.Timestamp(start_date)) & 
    (all_df['dteday'] <= pd.Timestamp(end_date))
]

# Pertanyaan 1: Bagaimana pengaruh musim terhadap jumlah peminjaman sepeda?
st.header("Jumlah peminjaman sepeda berdasarkan musim?")
st.dataframe(season_rentals)

# Visualisasi 1: Pengaruh Musim terhadap Peminjaman Sepeda
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=season_rentals.index, y=season_rentals.values, palette="coolwarm", ax=ax)
ax.set_title("Pengaruh Musim terhadap Jumlah Peminjaman Sepeda")
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Pertanyaan 2: Bagaimana pola peminjaman sepeda berdasarkan jam dalam sehari?
st.header("Jumlah peminjaman sepeda berdasarkan jam")
st.dataframe(hourly_rentals)

# Visualisasi 2: Peminjaman Sepeda Berdasarkan Jam
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker="o", ax=ax)
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Jam dalam Sehari")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Pertanyaan 3: Bagaimana pengaruh kondisi cuaca terhadap jumlah peminjaman sepeda?
st.header("Jumlah peminjaman sepeda berdasarkan kondisi cuaca")
st.dataframe(weather_rentals)

# Visualisasi 3: Pengaruh Cuaca terhadap Peminjaman
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=weather_rentals.index, y=weather_rentals.values, palette="coolwarm", ax=ax)
ax.set_title("Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Pertanyaan 4: Bagaimana distribusi jumlah peminjaman sepeda harian?
st.header("Statistik deskriptif jumlah peminjaman sepeda harian")
st.dataframe(all_df["cnt_day"].describe())

# Visualisasi 4: Distribusi Jumlah Peminjaman Sepeda Harian
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(all_df["cnt_day"], bins=30, kde=True, color="blue", ax=ax)
ax.set_title("Distribusi Jumlah Peminjaman Sepeda Harian")
ax.set_xlabel("Jumlah Peminjaman Sepeda")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

# Pertanyaan 5: Bagaimana pengaruh suhu terhadap jumlah peminjaman sepeda?
correlation = all_df[["temp_day", "cnt_day"]].corr().iloc[0, 1]
st.header(f"Korelasi antara suhu dan jumlah peminjaman sepeda: {correlation:.2f}")

# Visualisasi 5: Hubungan antara Suhu dan Peminjaman Sepeda
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=all_df["temp_day"], y=all_df["cnt_day"], alpha=0.5, ax=ax)
ax.set_title("Pengaruh Suhu terhadap Jumlah Peminjaman Sepeda")
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)
