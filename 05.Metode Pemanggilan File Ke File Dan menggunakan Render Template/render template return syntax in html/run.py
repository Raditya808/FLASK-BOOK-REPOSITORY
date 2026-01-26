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
