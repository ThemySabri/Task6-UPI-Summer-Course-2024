import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel files
data_jabar = pd.read_excel('data/sampah_jabar.xlsx')
data_jakarta = pd.read_excel('data/sampah_jakarta.xlsx')

# Add 'Province' column for both data
data_jabar['Provinsi'] = 'West Java'
data_jakarta['Provinsi'] = 'Jakarta'

# Combines both data
data = pd.concat([data_jabar, data_jakarta], ignore_index=True)

# Calculate the total annual waste generation in each province for each year
total_sampah_tahunan = data.groupby(['Provinsi', 'Tahun'])[
    'Timbulan Sampah Tahunan(ton)'].sum().reset_index()

# Calculate the average total annual waste generation in each province for all years
rata2_sampah_tahunan = data.groupby(
    'Provinsi')['Timbulan Sampah Tahunan(ton)'].mean().reset_index()

# Determine the province that produces the most annual waste generation each year
provinsi_terbanyak = total_sampah_tahunan.loc[total_sampah_tahunan.groupby(
    'Tahun')['Timbulan Sampah Tahunan(ton)'].idxmax()].reset_index(drop=True)

# Determine the province that produces the least annual waste generation each year
provinsi_tersedikit = total_sampah_tahunan.loc[total_sampah_tahunan.groupby(
    'Tahun')['Timbulan Sampah Tahunan(ton)'].idxmin()].reset_index(drop=True)

# Save analysis results to CSV file
total_sampah_tahunan.to_csv('total_sampah_tahunan.csv', index=False)
rata2_sampah_tahunan.to_csv('rata2_sampah_tahunan.csv', index=False)
provinsi_terbanyak.to_csv('provinsi_terbanyak.csv', index=False)
provinsi_tersedikit.to_csv('provinsi_tersedikit.csv', index=False)

# Create and save a graph of the total annual amount of waste in each province
plt.figure(figsize=(10, 6))
for provinsi in data['Provinsi'].unique():
    provinsi_data = total_sampah_tahunan[total_sampah_tahunan['Provinsi'] == provinsi]
    plt.plot(provinsi_data['Tahun'], provinsi_data['Timbulan Sampah Tahunan(ton)'], marker='o', label=provinsi)

plt.xlabel('Years')
plt.ylabel('Annual Waste Generation (ton)')
plt.title('Total Annual Amount of Waste in Each Province (2019-2023)')
plt.legend()
plt.grid(True)
plt.savefig('static/total_sampah_tahunan.png')
plt.close()

# Create and save a graph of the average annual waste generation in each province
plt.figure(figsize=(10, 6))
colors = ['green' if x <= 100000 else 'orange' if x <=
          700000 else 'red' for x in rata2_sampah_tahunan['Timbulan Sampah Tahunan(ton)']]
plt.bar(rata2_sampah_tahunan['Provinsi'],
        rata2_sampah_tahunan['Timbulan Sampah Tahunan(ton)'], color=colors)
plt.xlabel('Province')
plt.ylabel('Average Waste Generation (ton)')
plt.title('Average Annual Waste Generation in Each Province')
plt.savefig('static/rata2_sampah_tahunan.png')
plt.close()
