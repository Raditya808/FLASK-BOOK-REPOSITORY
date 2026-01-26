# File To File Flask Python 

<p>Pemanggilan File ke File dalam khasus OOP dalam Python Flask</p>



## Code 


```bash 
- Classtes.py
class testing:
    def __init__(self,nama='radit',asal='''jambi
    lalalalalalal
    '''):
        self.nama = nama 
        self.asal = asal 


    def setnama(self,nama):
        self.nama = nama 

    def setasal(self,asal):
        self.asal = asal 


# return 
    def hasilnama(self):
        return self.nama 

    def hasilasal(self):
        return self.asal

```





```bash 
- file run.py 
from flask import Flask , render_template 

from classtes import testing 

app = Flask(__name__)

@app.route('/')
def index():

    hasil_testclass= testing() 

    
    # kita mengirimkan hasil nya ke index namun 
    # kita tidak akan menaruh hasil function selff nya 
    # di dalam kode render template setelah index.html dibawah ini
    return render_template('index.html',h1=hasil_testclass)


if __name__ =="__main__":
    app.run(debug=True)

```

```bash
- file templates/index.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Rturn syntax in html</title>
  <link href="css/style.css" rel="stylesheet">
</head>

<body>
  <!-- Untuk mendaoatkan output yang tidak menghasilkan <none>
      kita perlu memanggil fuunction yang ada return
    </none>-->
  <h2>{{h1.hasilasal()}}</h2>
</body>

</html>
```
