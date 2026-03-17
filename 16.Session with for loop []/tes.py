import re
from flask import Flask, redirect,request,render_template,url_for,session

app = Flask(__name__)
app.secret_key = '123'



@app.route('/',methods=['GET','POST'])
def index():
    dataksng = []
    if request.method == 'POST':
        NAMA = session['nama'] = request.form['nama']
        UMUR = session['umur'] = request.form['umur']
        dataksng.append([NAMA,UMUR])
        #[NAMA=0,UMUR=1]
        for i in dataksng:
            return render_template('tes.html',i=i)
    # form untuk login mengikuti 
    else:
        return f"""
        <h1>Flask session with for loop</h1>
        <form method='POST'>
        <input type="text" name="nama" placeholder='masukann nama'><br>
        <input type="number" name="umur" placeholder="masukan umur"><br>
        <button type="submit">kirim</button>
        </form>
        """


@app.route('/del')
def hpuus():
    session.pop('nama',None)
    session.pop('umur',None)
    # ga bisa make render_template i tidak boleh kosong = undefined
    # return render_template('tes.html')
    # pake ini bir balik ke tampilan ngisi
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
