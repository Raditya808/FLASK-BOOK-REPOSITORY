from flask import Flask, render_template 
from classtes import artikel 


app = Flask(__name__)

@app.route('/')
def index():
    hasil = artikel()

    konten = 'Apa itu Python?!'    
    hasil.settnggl('23/01/2026')
   
    hasil.setknten('Flask oop dalam class pewaris')
    return render_template('index.html',h1 = konten,h2 = hasil.hasiltanggal(),h3 = hasil.hasilkonten())


if __name__ == "__main__":
    app.run(debug=True)
