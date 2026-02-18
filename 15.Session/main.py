# menggunakan list []
# namun tidak memanggil menggunakan index hanya menggunakan session syntax dari html

import re

from flask import Flask, redirect ,render_template,request, session,url_for


app = Flask(__name__)

# secret key sample untuk session syntax
app.secret_key = '123'


# rute tampilan awal
@app.route('/',methods=['GET','POST'])
def index():
    dataksng = []
    if request.method=='POST':
        # membuat session syntax untuk memanggil hasil
        # session[''] untuk ngirim hasil ke kode html 
        # request.form[] untuk mengirim metode POST ke kode html saat input
        nama = session['nm'] = request.form['nama']
        umur = session['umr'] = request.form['umur']
        dataksng.append([nama,umur]) 
        return render_template('index.html')
    # kondisi awal ketika masuk ke dalam port 5000
    else:
        return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Session witout for loop</title>
            </head>
            <body>
                <h1>Session syntax</h1>
                <form method="POST">
                <input type="text" name="nama" placeholder="masukan nama"><br>
                <input type="number" name="umur" placeholder="masukan umur"><br>
                <button type="submit">Kirim</button>
                </form>
            </body>
        </html>
        """


# hapus menggunakan pop dan None
# pada syntax khusus session
@app.route('/hapus')
def hapusdatanama():
    session.pop('nm',None)
    return render_template('index.html')

@app.route('/hapus2')
def hapusdataumur():
    session.pop('umr',None)
    return render_template('index.html')


if __name__ =="__main__":
    app.run(debug=True)
