import sqlite3
import os 
from flask import Flask, redirect,render_template,url_for,request
from class_test import daftarkehadiran

databaseisi  = os.getcwd() + '/newtes.db'

app = Flask(__name__)

@app.route('/')
def tabelkehadiran():
    conn = sqlite3.connect(databaseisi)
    cursor = conn.cursor()
    container = []
    for nomor,nama,kehadiran in cursor.execute('SELECT * FROM daftarkehadiran'): 
        model = daftarkehadiran(nomor,nama,kehadiran) 
        container.append(model)
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('index.html',container=container)
    
# tambah data dan memanggil function didalam class 
# tambah menggunakan constructors didalam class
@app.route('/tambah',methods=['GET','POST'])
def tambah():
    if request.method=='POST':
        nomor = int(request.form['nomor'])
        nama = request.form['nama']
        kehadiran = request.form['absen']
        model = daftarkehadiran(nomor,nama,kehadiran)
        model.tambah()
        return redirect(url_for('index'))
    else:
        return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Adding Datas</title>
            </head>
            <body>
                <h1></h1>
                <div class='adding-datas'>
                    <form method='POST'>
                    <!-- berdasarrkan konstruktor class -->
                    <input type="number" name="nomor" placeholder=""><br>
                    <input type="number" name="nomor" placeholder=""><br>
                    <button type="submit">kirim</submit>
                    </form>
                </div>
            </body>
        </html>

        """
        

if __name__=="__main__":
    app.run(port=5001,debug=True)

