# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Tambahkan konfigurasi
app.config['app.url'] = 'http://localhost'

@app.route('/landing')
def home():
    return render_template('landing.html')

@app.route('/produk')
def produk():
    return render_template('produk.html')

@app.route('/berita')
def berita():
    return render_template('berita.html')

@app.route('/prediksi')
def prediksi():
    return render_template('prediksi.html')

@app.route('/return.html')
def return1():
    stock = request.args.get('stock')
    predictions = {
        'BBRI': 'naik',
        'BBCA': 'turun',
        'BMRI': 'naik',
        'GOTO': 'turun'
    }
    prediction = predictions.get(stock, 'tidak ditemukan')
    return render_template('return.html', stock=stock, prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)