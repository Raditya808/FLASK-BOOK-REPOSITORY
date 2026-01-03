## wsgiref application


<p>Cara kerja wsgiref dalam lingkungan aplikasi
Kode ini adalah contoh dasar WSGI (Web Server Gateway Interface) - standar komunikasi antara web server dan aplikasi web Python. Ini menunjukkan cara kerja framework seperti Flask/Django "di balik layar".
</p>


## OUTPU ON BROWSER 
<img src="http port 5000.png">



## Code


```bash 
from wsgiref.simple_server import make_server 

def application(environ,make_resoponse):
    body = [
    '%s: %s' %(key,value) for key,value \
    in sorted(environ.items())
    ]
    
    body = '\n'.join(body)

    status = '200 OK'
  
    headers = [ 
    ('Content-Type','text/plain'),
    ('Content-Length',str(len(body)))
    ]
    
    make_server(status,headers)
    return [body.encode('utf-8')]
    
```



## Code to run



```bash 
if __name__ =="__main__":
  server = make_server('localhost',5000,application)
  server.serve_forever()
````


## run on port 



```bash 
on browser

http://localhost:5000 

```



