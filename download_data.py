import pandas as pd

# Download data from link
url = 'https://sipsn.menlhk.go.id/sipsn/public/data/timbulan'
data = pd.read_html(url)[0]

# Save data to CSV file for convenience
data.to_csv('timbulan_sampah.csv', index=False)
