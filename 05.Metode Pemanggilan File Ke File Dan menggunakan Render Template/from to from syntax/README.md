# File To File Flask Python 

<p>Pemanggilan File ke File dalam khasus OOP dalam Python Flask</p>



## Code 


```bash 
file app.py
# membuat class halo dunia 
class halodunia:
    # membuat function self dengan nilai return format str halo dunia
    def __init__(self):
        # membuat self pada variabel_hasil halo 
        # atau menggunakan syntax html juga bisa 
        self.hasil_halo =  f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>HALO FILE TO FILE</title>
            </head>
            <body>
                <div>
                    <h1>FILE TO FILE SYNTAX FLASK</h1>
                    <p>
                     file to file 
                    </p>
                    <p>
                    file to file 
                    </p>
                </div>
            </body>
        </html>
        """


    # output 
    def hasil(self):
        # mengirim hasil 
        return self.hasil_halo

```





```bash 
file run.py 

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


```

