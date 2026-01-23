# File Render Template Flask

<p>Pemanggilan File menggunakan render_template</p>



## Code 


```bash 
file main.py
from flask import Flask,render_template 

testing = Flask(__name__)

@testing.route('/')
def index():
    # menggunakan render_template untuk memanggil file html
    return render_template("hello.html")

if __name__=="__main__":
    testing.run(debug=True)

```





```bash 
file templates/hello.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>render template syntax</title>
  <link href="css/style.css" rel="stylesheet">
</head>

<body>
  <h1 style="text-align: center;">Halo dunia dari render template syntax flask</h1>
</body>

</html>
```

