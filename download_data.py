import pandas as pd

# Unduh data dari tautan
url = 'https://sipsn.menlhk.go.id/sipsn/public/data/timbulan'
data = pd.read_html(url)[0]

# Menyimpan data ke file CSV untuk kemudahan
data.to_csv('timbulan_sampah.csv', index=False)
