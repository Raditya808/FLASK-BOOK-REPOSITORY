from flask import Flask 

# import file app dan class halo dunia
from app import halodunia 


app = Flask(__name__)

@app.route('/')
def index():
    # membuat variabel bernama model_syntax
    model_syntax = halodunia()

    # mengembalikan nilai model_syntax.hasil() hasil dari file app.py 
    # dari function hasil(self)
    return model_syntax.hasil()

# jalankan file 
if __name__=="__main__":
    app.run(debug=True)


