from flask import Flask,render_template,request

# mengimport file classtes.py dan class bernama lgtes
from classtes import lgtes
    
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    tes = lgtes()
    if request.method =='POST':
        # membuat var bernama username agar dikirim lewat request.form sebagai parameter username untuk html log.html dan begitu juga dengan password
        username = request.form['username']
        password = request.form['password']
        tes.setnama(username)
        tes.setpassword(password)
        if tes.autentikasi():
            # mengirim var tes yang berisi object lgtes dari classtes.py ke html agar kita bisa mengirim parameter function dari classtes agar bisa memasukan object function bernama dapat_nama ke file html sukses.html
            # kondisi dibawah ini jika true maka akan masuk ke sukses.html
            return render_template('sukses.html',tes=tes)
        # kondisi dibawah ini jika tidak true / false maka akan masuk di error.html
        else:
            return render_template('error.html')
    # kondisi dibawah ini kita akan masuk ke index.html untuk login
    return render_template('log.html')
if __name__ =="__main__":
    app.run(debug=True)
