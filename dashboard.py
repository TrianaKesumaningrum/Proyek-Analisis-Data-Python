import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memasukkan data tabel
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')
bikesharing_df = day_df.merge(hour_df, on='dteday', how='inner', suffixes=('_day', '_hour'))

# Menampilkan data penyewaan sepeda
avg_holiday = day_df.groupby('holiday')['cnt'].mean()
avg_weekday = day_df.groupby('weekday')['cnt'].mean()

labels_holiday = ['Hari Libur', 'Hari Tidak Libur']
labels_weekday = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

st.write("## Rata-rata Penyewaan Sepeda")
st.write("### Rata-rata Penyewaan Sepeda pada Hari Libur")
st.write(avg_holiday)
st.write("### Rata-rata Penyewaan Sepeda pada Hari dalam Seminggu")
st.write(avg_weekday)

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

axes[0].pie(avg_holiday, labels=labels_holiday, autopct='%1.1f%%', colors=('#ff8fab', '#ffc2d1'))
axes[0].set_title('Rata-rata Penyewaan Sepeda pada Hari Libur')

axes[1].pie(avg_weekday, labels=labels_weekday, autopct='%1.1f%%', colors=('#ddb892', '#b08968', '#7f5539', '#9c6644'))
axes[1].set_title('Rata-rata Penyewaan Sepeda pada Hari dalam Seminggu')

st.pyplot(fig)


# Menampilkan data penyewaan sepeda berdasarkan kondisi cuaca
weathersit_labels = {
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan',
}
bikesharing_df['weathersit_label'] = bikesharing_df['weathersit_day'].map(weathersit_labels)


avg_weather = bikesharing_df.groupby('weathersit_label')['cnt_day'].mean().reset_index()

st.write("## Rata-rata Penyewaan Sepeda berdasarkan Kondisi Cuaca")
st.write(avg_weather)

plt.figure(figsize=(10, 7))
sns.barplot(data=avg_weather, x='weathersit_label', y='cnt_day', color='#ff8fab')

plt.title('Rata-rata Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')

plt.xticks(rotation=45)

st.pyplot(plt)


# Menampilkan data penyewaan sepeda berdasarkan kondisi musim
season_labels = {
    1: 'Dingin',
    2: 'Semi',
    3: 'Panas',
    4: 'Gugur',
}
bikesharing_df['season_label'] = bikesharing_df['season_day'].map(season_labels)
avg_season = bikesharing_df.groupby('season_label')['cnt_day'].mean().reset_index()

st.write("## Rata-rata Penyewaan Sepeda berdasarkan Kondisi Musim")
st.write(avg_season)

plt.figure(figsize=(10, 7))
sns.barplot(data=avg_season, x='season_label', y='cnt_day', color='#ff8fab')

plt.title('Rata-rata Jumlah Pengguna Sepeda berdasarkan Kondisi Musim')
plt.xlabel('Kondisi Musim')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')

plt.xticks(rotation=45)

st.pyplot(plt)


# Menampilkan data penggunaan sepeda (terdaftar dan tidak terdaftar)
st.write("## Penggunaan Sepeda Terdaftar dan Tidak Terdaftar")

total_terdaftar = day_df['registered'].sum()
total_tidak_terdaftar = day_df['casual'].sum()

st.write("Total sewa sepeda (terdaftar):", total_terdaftar)
st.write("Total sewa sepeda (tidak terdaftar):", total_tidak_terdaftar)

cnt_bikesharing = [day_df['registered'].sum(), day_df['casual'].sum()]

labels = ['Terdaftar', 'Tidak Terdaftar']

plt.figure(figsize=(8, 6))
plt.barh(labels, cnt_bikesharing, color=['#ff8fab', '#ffccd5'])

plt.title('Total Sewa Sepeda (Terdaftar dan Tidak Terdaftar)')
plt.xlabel('Jumlah')
plt.ylabel('Tipe Sewa Sepeda')

st.pyplot(plt)
