
# wsgi

<p> apa itu wsgi?  web server gateaway interface merupakan modul web server, module python
framework application programming interface (API) atau shoftware. wsgi hanya sekedar 
spesifikasi antarmuka yang menjelaskan bagaimana seharusnya aplikasi dapat berkomunikasi dengan web server.</p>


<p>untuk membuat wsgi kita akan terlebih dahulu mengenali syntax nya</p>
<p>membuat impor fungsi make_server  yang di sediakan oleh python</p>

```bash
from wasgiref.simple_server import make_server
```

<p>memabuat fungsi yang berisi kode html</p>

```bash
def application(environ,start_response):
body = '''
<html> Ini berisi tag tag html</html>
'''
status = '200 OK'
headers = [
    ('Content-type','text/html')
    ('Content-length',str(len(body)))
]
server = start_response(headers,status)
return [body.encode('utf-8')] 
```


<p>menjalankan file dengan port 5000</p>

```bash 
if __name__ =="__main__":
server = make_server('localhost',5000,application)
server.serve.forever()
```

<p>jalankan di terminal file nya menggunkan package python dengan port</p>

```bash 
http://locallhost:5000
```
