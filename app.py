# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Tambahkan konfigurasi
app.config['app.url'] = 'http://localhost'

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/produk')
def produk():
    return render_template('produk.html')

@app.route('/berita')
def berita():
    return render_template('berita.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)