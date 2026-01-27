# Class Lingkaran

<p>Belajar Menghitung Luas dan keliling Lingkaran
</p>



## Code 

```bash 
-file run.py 
from flask import Flask,render_template ,redirect,request

from clastes import lingkaran

app = Flask(__name__)

@app.route('/')
def index():
    # membuat var baru dan memanggil class lingkaran() di clastes.py
    hasil = lingkaran()
    
    #  set nilai dari function self set_radius dari clastes
    hasil.set_radius(5.0)
    # di kirim ke index.html dan hasil.setradius(5.0) nya yang di timpa
    # dengan mengirim hasil dari set_radius diatas ke file html
    return render_template('index.html',hasil=hasil)


    
if __name__=="__main__":
    app.run(debug=True)


```


```bash
- clastes.py
from math import pi 

class lingkaran:
    def __init__(self):
        self.radius = 0 

    def set_radius(self,r):
        self.radius = r 

        # hasil yang akan di kirim ke html
    def get_radius(self):
        return self.radius

        # hasil yang akan di kirim ke html
    def hitungluas(self):
        return pi * (self.radius **2)

        # hasil yang akan di kirim ke html
    def hitungkeliling(self):
        return 2 * pi * self.radius
```


```bash
- templates/index.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>hasil</title>
  <link href="css/style.css" rel="stylesheet">
</head>

<body>
  <h1>Hitung Lingkaran</h1>
  <!-- memanggil hasil yang di run.py lalu memanggil objek get_radius di run.py jadi 5.0 karena di run.py set_radius = 5.0 dan objek get_radius di dapatkan 5.0 di return -->
  <p>Jari jari = {{hasil.get_radius()}}</p>
  <!-- hasil tadi akan di panggil hitungkeliling() di objek return di ruun.py hitung keliling maka nilai 5.0 tadi akan di hitung menggunakan rumus pi -->
  <p> keliling = {{hasil.hitungkeliling()}}</p>
  <!-- hasil tadi akan dipanggil luas di objek hitungluas di return di run.py maka keliling 5.0 akan di hitung menggunakan rumus 2*pi*self_radius maka itu hasilnya -->
  <p>luas {{hasil.hitungluas()}}</p>
</body>

</html>
```
