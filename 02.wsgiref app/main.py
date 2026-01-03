# aplikasi wsgi sederhana  
# bagaimana cara kerja wsgi python bekerja sebelum web framework flask dan django ada 
# dibuat menggunakan library wsgiref python standard library
# cara kerja wsgi menerima request dari browser kemudian mengirim response ke browser

from wsgiref.simple_server import make_server 

def application(environ,make_response): 
# membuat function yang didalam nya menerima parameter environ dan make_resoponse
    body = [ 
        '%s: %s' %(key, value) for key,value \
        in sorted(environ.items()) # elemen elemen dicitionary akan di urutkan menggunakan fungsi sorted() 
                 # kata kunci environ.items() akan mengembalikan objek dicitionary yang berisi seluruh variabel lingkungan dalam objek dicitionary tersebut nama variabel akan dijadikan sebagai kunci (key) dan isi variabel sebagai nilai (value) dari objek dicitionary        
    ]

    body = '\n'.join(body)

    status = '200 OK' # mengirim metadata response ke browser 
    
    headers = [

    ('Content-Type','text/plain'), # jenis data yang dikirim ke browser sebagai teks biasa
    ('Content-Length',str(len(body)))
    ]
    make_response(status,headers)
    return[body.encode('utf-8')] 

if __name__=="__main__":
    server = make_server('localhost',5000,application)
    server.serve_forever()

# membuat http server  
# dijalankan localhost http://localhost:5000 
# pakai fungsi application sebaga wadah wsgiref 
