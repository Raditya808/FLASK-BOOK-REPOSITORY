from flask import Flask,render_template

# didalam python flask kita bisa mengirim variabel menggunakan render_template 
# lalu kalau variabel nya memiliki value tipe data integer 
# maka kita bisa mengirimkan jinja dan kita hitung dari variabel itu 


app = Flask(__name__)


@app.route('/')
def index_route():
    a = 10 
    b = 25
    return render_template('index.html',a=a,b=b)


if __name__ == "__main__":
    app.run(debug=True)
