# Class Login

<p>Membuat Class login yang ada password dan username 
</p>



## Code 

```bash
-file main.py
from flask import Flask,render_template,request
from classtes import User  

app =Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    models = User() 
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        
        # models.setUsername adalah objek function yang ada di classtes.py
        models.setUsername(username)
        # models.setUsername adalah objek function yang ada di classtes.py
        models.setPassword(password)

        # models dari variabel diatas authenticate adalah dari class function bernama authenticate
        # kondisi if jika user dan password sesuai maka masuk di login_success.html
        if models.authenticate():
            return render_template('login_success.html',models=models)
        # kondisi jika username dan password tidak sesuai maka error di error.html
        else:
            return render_template('error.html')
    # masuk ke tampilan awal web untuk login di login.html    
    else:
        return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)
```



```bash 
-file classtes.py
class User(object):
    def __init__(self,username="",password=""):
        self.username = username
        self.password = password
        self.label = {
                "username": "Username:",
                "password": "Password:"
        }
    
    def setUsername(self,username):
        self.username = username 

    def setPassword(self,password):
        self.password = password
    
    def dapat_username(self):
        return self.username


    # kondisi jika true dimana function authenticate dan memanggil self.username di set demo dan self.password adalah flask maka user bisa masuk
    # jika false maka akan diarahkan ke web lain / 
    def authenticate(self):
        if self.username == "demo" and  self.password == 'flask':
            return True 
        else:
            return False


```



```bash
- templates/login.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Login with usr authenticate with pw in python</title>
  <link href="css/style.css" rel="stylesheet">
</head>

<body>
  <h1>Welcome</h1>
  <form method="POST">
    <input type="text" name="username" placeholder="Masukan username"><br>
    <input type="text" name="password" placeholder="Masukan password"><br>
    <input type="submit" value="kirim">
  </form>
</body>

</html>
```


```bash
- templates/login_success.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>sukses</title>
  <link href="css/style.css" rel="stylesheet">
</head>

<body>
  <h1>Halo</h1>
<!-- models adalah file yang berada di main.py dapat_username adala objek function yang ada di classtes.py-->
  <p>Halo <strong>{{models.dapat_username()}}</strong></p>
</body>

</html>
```


```bash
- templates/error.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title></title>
  <link href="css/style.css" rel="stylesheet">
</head>

<body>
  <h1 style="text-align: center;">ERROR 404</h1>
</body>

</html>
```
