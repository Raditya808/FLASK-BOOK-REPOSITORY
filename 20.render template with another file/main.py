from flask import Flask,render_template



app = Flask(__name__)



# flask selagi file templates bisa di isi dengan file lain 
@app.route('/')
def index():
    """ rute file bernama html1 dan didalam nya ada file html"""
    return render_template('html1/html1.html') # maka outpuut di browser akan Halo dunia


app.run(port=5001,debug=True)
