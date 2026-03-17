# metode flask dalam render template dalam rute yang sama menggunakan 
# return di variabel yang sama menggunakan +=

# contoh 
from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def gabungan():
    # membuat variabel dan assignment dan memanggil isi html dan di return 
    # tentuin arah file utama yang digabungin 
    # lalu variabel yang sama menggunakan += dan render templates dari file lain
    
    # rute utama untuk gabung 
    testgabng = render_template('index1.html')

    # rute kedua untuk gabung di file html lain
    testgabng += render_template('index2.html')

    # rute ketiga untuk gabung di file html.lain 
    testgabng += render_template('index3.html')

    # nilai di return untuk hasil
    return testgabng
    
    

    # maka dalam satu file kita bisa menggabungkan file html menggunakan +=


# jalankan di port 5000
# lewat terminal
if __name__=="__main__":
    app.run(debug=True)
