import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with st.sidebar:
    st.image("logo.png")
    
# Load Data
def load_data():
    day = pd.read_csv("day.csv")  # Pastikan file CSV tersedia di direktori yang sama
    hour = pd.read_csv("hour.csv")
    
    return day, hour

day, hour = load_data()

# Title
st.title('Rental Bike Dashboard :sparkles:')

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
def load_data():
    day = pd.read_csv("day.csv")  # Pastikan file CSV tersedia di direktori yang sama
    hour = pd.read_csv("hour.csv")
    return day, hour

day, hour = load_data()

# Title
st.title("Dashboard Peminjaman Sepeda")

# Sidebar Filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", ['All', 'Spring', 'Summer', 'Fall', 'Winter'])

df = day.copy()
if selected_season != 'All':
    season_map = {'Spring': 1, 'Summer': 2, 'Fall': 3, 'Winter': 4}
    df = df[df['season'] == season_map[selected_season]]

# Visualisasi 1: Pengaruh Musim terhadap Peminjaman Sepeda
st.subheader("Pengaruh Musim terhadap Peminjaman Sepeda")
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=df, estimator=sum, palette='coolwarm', ax=ax)
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

# Visualisasi 2: Peminjaman Sepeda Berdasarkan Jam
st.subheader("Peminjaman Sepeda Berdasarkan Jam")
fig, ax = plt.subplots()
sns.lineplot(x='hr', y='cnt', data=hour, estimator=sum, ci=None, marker="o", color="b", ax=ax)
ax.set_xticks(range(0, 24))
st.pyplot(fig)

# Visualisasi 3: Pengaruh Cuaca terhadap Peminjaman
st.subheader("Distribusi Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots()
sns.boxplot(x='weathersit', y='cnt', data=day, palette='Set2', ax=ax)
ax.set_xticklabels(["Cerah", "Mendung", "Hujan Ringan", "Hujan Lebat"])
st.pyplot(fig)

# Visualisasi 4: Hubungan Suhu dengan Peminjaman
st.subheader("Hubungan antara Suhu dan Peminjaman Sepeda")
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=day, alpha=0.5, color='r', ax=ax)
st.pyplot(fig)

# Visualisasi 5: Histogram Distribusi Peminjaman Harian
st.subheader("Distribusi Jumlah Peminjaman Sepeda Harian")
fig, ax = plt.subplots()
sns.histplot(day['cnt'], bins=20, kde=True, color='c', ax=ax)
st.pyplot(fig)

st.sidebar.write("Dashboard ini dibuat dengan Streamlit untuk menganalisis data peminjaman sepeda.")
