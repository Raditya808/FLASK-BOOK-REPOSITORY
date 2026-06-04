from flask import Flask,render_template 



app= Flask(__name__)


@app.route('/')
def main():
    # pembuatan variabel bisa dari file main.py atau bisa dari file html 
    a = 10 
    return render_template('main.html',a=a)



if __name__=="__main__":
    app.run(debug=True)
