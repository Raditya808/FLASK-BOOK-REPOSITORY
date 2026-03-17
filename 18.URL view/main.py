# dalam python untuk ke rute web dengan parameter kita bisa menggunakan <parameter> setelah rute / 
# contoh : /user/<username> maka kita bisa mengakses username dengan menggunakan parameter username 
# dan dengan function yang membungkus route dan parameter tersebut 
# sehingga kita bisa mengakses username dengan menggunakan %s' % username 


# contoh
# dengan function dan parameter yang sama di akse smenggunakan %


from flask import Flask,url_for

app = Flask(__name__)


# ini rute tanpa slash otomatis maka akan mengeluarkan output langsung
# dan bisa juga menggunakan tag heading 
@app.route('/')
def index():
    return f"<h1>Hello world</h1>"


# rute kedua menggunakan % dan function dengan parameter dan rute parameter
@app.route('/hello/<name>')
def index2(name):
    return 'Hello %s' % name


if __name__=="__main__":
    app.run(debug=True)
