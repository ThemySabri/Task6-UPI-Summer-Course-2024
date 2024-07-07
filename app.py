from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    # Read data from CSV files
    total_sampah_tahunan = pd.read_csv('total_sampah_tahunan.csv')
    rata2_sampah_tahunan = pd.read_csv('rata2_sampah_tahunan.csv')
    provinsi_terbanyak = pd.read_csv('provinsi_terbanyak.csv')
    provinsi_tersedikit = pd.read_csv('provinsi_tersedikit.csv')

    return render_template('index.html',
                           total_sampah_tahunan=total_sampah_tahunan,
                           rata2_sampah_tahunan=rata2_sampah_tahunan,
                           provinsi_terbanyak=provinsi_terbanyak,
                           provinsi_tersedikit=provinsi_tersedikit)


if __name__ == '__main__':
    app.run(debug=True)
