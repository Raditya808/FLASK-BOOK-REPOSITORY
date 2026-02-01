import sqlite3
from flask import Flask, redirect,render_template,request,url_for,session
from models import produk 
import sqlite3
import os 

app = Flask(__name__)

# memanggil file dari models.py
# disini kita memanggil os.getcwd sebagai variabel databasename lalu memanggil file dbtest.db di file sebagai str 
# lalu memanggil cursor = conn.cursor() sebagai objek yang akan di panggil isi dari isi database file dbtest.dbtest
# lalu membuat variabel bernama container dan menggunakan list dan membungkkus kode,nama,harga dalam satu data menggunakan for loop 
# lalu di masukan menggunakan cursor.execute dari library sqlite3 dan menggunakan syntax sql SELECT * FROM produk yaitu mengambil value database tabel bernama produk 
# lalu membuat variabel bernama model lalu class produk dipanggil dan membungkkus kode nama dan harga lalu container.append(model) membungkys model sebagai append untuk di simpan di list 
# cursor.close() tutup cursor 
# conn.close() tutup cone 
# return render_template kirim ke file index.html dan container
@app.route('/')
def index():
    # ketika databae ada didalam file kita terlebih menggunakan slash untuk memanggil db nya
    databasename = os.getcwd() + '/dbtest.db'
    conn = sqlite3.connect(databasename)
    cursor = conn.cursor()
    container = []
    for kode,nama,harga in cursor.execute("SELECT * FROM produk"):
        model = produk(kode,nama,harga)
        container.append(model)
    cursor.close()
    conn.close()
    return render_template('index.html',container=container)




# tambah data dari function tambah dari file models.
@app.route('/tambah',methods=['GET','POST'])
def tambah():
    if request.method=='POST':
        kode =  int(request.form['kode'])
        nama =  request.form['nama']
        harga = int(request.form['harga'])
        model = produk(kode,nama,harga)
        model.tambah()
        return redirect(url_for('index'))
    else:
        return render_template('tambah.html')


# mengedit isi dari kode nama dan harga 
@app.route('/ubah/<int:id>',methods=['GET','POST'])
def ubah(id):
    # parameter model yang di isi dari objek konstruktor dari class bernama produk()
    # dan menerima parameter id dari function ubah(id)
    model = produk() 
    model.load(id)

    if request.method=='POST': 
        kode = int(request.form['kode'])
        nama = request.form['nama']
        harga = int(request.form['harga'])

    # dipanggil function sebaga objek model set harga dari function set di models.py
        model.setkode(kode)
        model.setnama(nama)
        model.setharga(harga)
        model.ubah()
        return redirect(url_for('index'))

    else:
        return render_template('ubah.html',model=model)

if __name__=="__main__":
    app.run(debug=True)
