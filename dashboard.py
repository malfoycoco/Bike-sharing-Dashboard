import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

day_df = pd.read_csv("https://github.com/malfoycoco/Bike-sharing-kaggle/raw/refs/heads/main/day.csv")
hour_df = pd.read_csv("https://github.com/malfoycoco/Bike-sharing-kaggle/raw/refs/heads/main/hour.csv")

df = day_df  

weekday_mapping = {
    0: "Minggu", 1: "Senin", 2: "Selasa", 3: "Rabu",
    4: "Kamis", 5: "Jumat", 6: "Sabtu"
}


df["weekday"] = df["weekday"].map(weekday_mapping)

st.sidebar.header("Filter Data")
selected_day = st.sidebar.selectbox("Pilih Hari", df["weekday"].unique())

filtered_df = df[df["weekday"] == selected_day]

st.title("Dashboard Penyewaan Sepeda 🚴")

#Visualisasi 1: Bar Chart Penyewaan Sepeda per Hari 
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari")
order = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
df["weekday"] = pd.Categorical(df["weekday"], categories=order, ordered=True)

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(data=df, x="weekday", y="cnt", palette="viridis", ax=ax)
plt.xlabel("Hari dalam Seminggu")
plt.ylabel("Jumlah Penyewaan Sepeda")
plt.xticks(rotation=45)
st.pyplot(fig)  

#Visualisasi 2: Scatter Plot Suhu & Kecepatan Angin 
st.subheader("Pengaruh Suhu dan Kecepatan Angin terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8,5))
sc = sns.scatterplot(data=df, x="atemp", y="cnt", hue="windspeed", palette="viridis", ax=ax)
plt.xlabel("Suhu (atemp)")
plt.ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

st.subheader(f"Tabel Data Penyewaan Sepeda ({selected_day})")
st.write(filtered_df.head())  # Menampilkan beberapa baris pertama data setelah difilter
