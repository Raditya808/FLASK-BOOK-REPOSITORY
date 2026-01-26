from flask import Flask,render_template ,redirect,request

from clastes import lingkaran

app = Flask(__name__)

@app.route('/')
def index():
    hasil = lingkaran()
    
    #  set nilai dari function self set_radius dari clastes
    hasil.set_radius(5.0) 
    return render_template('index.html',hasil=hasil)


    
if __name__=="__main__":
    app.run(debug=True)

