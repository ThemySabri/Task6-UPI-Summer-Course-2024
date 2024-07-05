import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file Excel
data_jabar = pd.read_excel('data/sampah_jabar.xlsx')
data_jakarta = pd.read_excel('data/sampah_jakarta.xlsx')

# Menambahkan kolom 'Provinsi' untuk kedua data
data_jabar['Provinsi'] = 'Jawa Barat'
data_jakarta['Provinsi'] = 'DKI Jakarta'

# Menggabungkan kedua data
data = pd.concat([data_jabar, data_jakarta], ignore_index=True)

# Menghitung total timbulan sampah tahunan di setiap provinsi untuk setiap tahun
total_sampah_tahunan = data.groupby(['Provinsi', 'Tahun'])[
    'Timbulan Sampah Tahunan(ton)'].sum().reset_index()

# Menghitung rata-rata total timbulan sampah tahunan di setiap provinsi untuk semua tahun
rata2_sampah_tahunan = data.groupby(
    'Provinsi')['Timbulan Sampah Tahunan(ton)'].mean().reset_index()

# Menentukan provinsi yang menghasilkan timbulan sampah tahunan terbanyak setiap tahun
provinsi_terbanyak = total_sampah_tahunan.loc[total_sampah_tahunan.groupby(
    'Tahun')['Timbulan Sampah Tahunan(ton)'].idxmax()].reset_index(drop=True)

# Menentukan provinsi yang menghasilkan timbulan sampah tahunan paling sedikit setiap tahun
provinsi_tersedikit = total_sampah_tahunan.loc[total_sampah_tahunan.groupby(
    'Tahun')['Timbulan Sampah Tahunan(ton)'].idxmin()].reset_index(drop=True)

# Menyimpan hasil analisis ke file CSV
total_sampah_tahunan.to_csv('total_sampah_tahunan.csv', index=False)
rata2_sampah_tahunan.to_csv('rata2_sampah_tahunan.csv', index=False)
provinsi_terbanyak.to_csv('provinsi_terbanyak.csv', index=False)
provinsi_tersedikit.to_csv('provinsi_tersedikit.csv', index=False)

# Membuat dan menyimpan grafik jumlah total sampah tahunan di setiap provinsi dari tahun ke tahun
plt.figure(figsize=(10, 6))
for provinsi in total_sampah_tahunan['Provinsi'].unique():
    df_provinsi = total_sampah_tahunan[total_sampah_tahunan['Provinsi'] == provinsi]
    plt.plot(df_provinsi['Tahun'],
             df_provinsi['Timbulan Sampah Tahunan(ton)'], label=provinsi)

plt.xlabel('Tahun')
plt.ylabel('Timbulan Sampah (ton)')
plt.title('Jumlah Total Sampah Tahunan di Setiap Provinsi')
plt.legend()
plt.savefig('static/total_sampah_tahunan.png')
plt.close()

# Membuat dan menyimpan grafik rata-rata timbulan sampah tahunan di setiap provinsi
plt.figure(figsize=(10, 6))
plt.bar(rata2_sampah_tahunan['Provinsi'], rata2_sampah_tahunan['Timbulan Sampah Tahunan(ton)'], color=[
        'green' if x <= 100000 else 'orange' if x <= 700000 else 'red' for x in rata2_sampah_tahunan['Timbulan Sampah Tahunan(ton)']])
plt.xlabel('Provinsi')
plt.ylabel('Rata-rata Timbulan Sampah (ton)')
plt.title('Rata-rata Timbulan Sampah Tahunan di Setiap Provinsi')
plt.savefig('static/rata2_sampah_tahunan.png')
plt.close()
