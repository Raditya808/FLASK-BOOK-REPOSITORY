from flask import Flask

application = Flask(__name__)


# rute yang tidak ada parameter
@application.route('/')
def index():
    return f"hello from flask"

# rute dengan name 
# memanggil hasil menggunakan %
# /hello/radit
@application.route('/hello/<name>')
def index2(name):
    return f"<h1>Halo %s</h1>" % name

# rute dengan integer 
# number 
@application.route('/number/<angka>')
def index3(angka):
    return f"<h1>Page %s</h1>" %angka



if __name__=="__main__":
    application.run(debug=True)
