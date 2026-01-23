from flask import Flask, render_template
from classtest import halosyntax

app = Flask(__name__)

@app.route('/')
def index_hasil():

    # class halosyntax 
    hasil_route = halosyntax()
   
   # memanggil method hasil dari class halosyntax
   # lalu dikirim ke template success.html
    hasil_route = hasil_route.hasil()
    return render_template('success.html',hasil_route=hasil_route)


if __name__=="__main__":
    app.run(debug=True)
