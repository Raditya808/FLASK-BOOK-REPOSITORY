from wsgiref.simple_server import make_server 

def application(environ,start_response):
    body = '''<html>
                <head>
                <title>demo wsgi</title>
                </head>
                <h1>Halo dunia dari wsgi</h1>
                </html>'''
    status = '200 OK'
    headers = [
        ('Content-type','text/html'),
        ('Content-lenght',str(len(body)))
    ]
    start_response(status,headers)
    return [body.encode('utf-8')] # diganti dari [body] mengunakan encode return [body.encode('utf-8')]
if __name__ == "__main__":
    server = make_server('localhost',5000,application) # dijalankan port http://locallhost:5000
    server.serve_forever()