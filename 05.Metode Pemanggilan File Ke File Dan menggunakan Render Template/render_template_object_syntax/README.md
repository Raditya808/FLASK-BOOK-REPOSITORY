# File To File Flask Python 

<p>Pemanggilan file menggunakan render_template dan mengirim hasil class</p>



## Code 


```bash 
file classtest.py 
class halosyntax:
    def __init__(self):
        self.test1 = 'halo dunia'

    def hasil(self):
        return self.test1

```





```bash 
file run.py
from flask import Flask, render_template
# memanggil nama file classtest.py dan mengimport class halosyntax dari file tersebut
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
```




```bash 
file templates/success.html 
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Object Class Flask Render Template</title>
  <link href="css/style.css" rel="stylesheet">
</head>

<body>
  <!-- memanggil hasil_route di file run.py-->
  <h1>{{hasil_route}}</h1>
</body>


</html>
```
```
