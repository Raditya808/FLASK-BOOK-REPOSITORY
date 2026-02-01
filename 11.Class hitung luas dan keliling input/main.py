import re
from flask import Flask ,render_template,request
# class hitungluas dan hitunglebar dari file classtes.py
from classtes import hitungluas,hitungkeliling


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hitung_luas():
    if request.method =='POST':
        tes = float(request.form['luas'])
        
        # memanggil object hitungluas dari import classtes.py yang berisi class bernama hitungluas  
        # dan memberi nama variabel bernama htung_luas dan memanggil import hitungluas itu agar bisa memanggil variabel tes yang di konversi ke float yang dikirim ke form html lewat request.form 
        htung_luas = hitungluas(tes)
        return render_template('hasil_luas_.html',htung_luas=htung_luas)
    return render_template('input_luas.html')

@app.route('/hitung_lebar',methods=['GET','POST'])
def hasil_lebar():
    if request.method=='POST':
        tes2 = float(request.form['keliling'])
        
        # memanggil object hitungkeliling dari import classtes.py yang berisi class bernama hitungkeliling 
        # dan memberi nama variabel bernama hasil_keliling dan memanggil import hitungkeliling itu agar bisa memanggil variabel tes yang di konversi ke float yang dikirim ke form html lewat request.form
        hasil_keliling = hitungkeliling(tes2)
        return render_template('hasil_keliling.html',hasil_keliling=hasil_keliling)
    return render_template('input_keliling.html')

        


if __name__ =="__main__":
    app.run(debug=True)
