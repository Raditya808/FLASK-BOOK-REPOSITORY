from flask import Flask,render_template 

testing = Flask(__name__)

@testing.route('/')
def index():
    return render_template("hello.html")

if __name__=="__main__":
    testing.run(debug=True)
