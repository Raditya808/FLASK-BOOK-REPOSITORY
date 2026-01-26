# File To File Flask Python 

<p>Pemanggilan File ke File dalam khasus OOP dalam Python Flask menggunakan variabel di render templates</p>



## Code 


```bash 
-file classtes.py
class artikel:
    
    # function self parameter 
    def sethding(self,heading):
        self.heading = heading

    def settnggl(self,tanggal):
        self.tanggal = tanggal 

    
    def setknten(self,konten):
        self.konten = konten

        
    # function hasil return
    def hasilheading(self):
        return self.heading

    def hasiltanggal(self):
        return self.tanggal 

    
    def hasilkonten(self):
        return self.konten
        """


    # output 
    def hasil(self):
        # mengirim hasil 
        return self.hasil_halo

```





```bash 
-file run.py 
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


```


```bash
-file templates/index.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SET OBJECT CLASS FLASK</title>
  <link href="css/style.css" rel="stylesheet">
</head>

<body>
  <h1>{{h1}}</h1>
  <p>{{h2}}</p>
  <p>{{h3}}</p>
</body>

</html>
```

