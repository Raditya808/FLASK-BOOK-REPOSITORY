
from flask import Flask,request


app = Flask(__name__)

@app.route('/')
def index():
    headers = request.headers

    response = [
    '%s %s' % (key,value) for key,value in sorted(headers.items())
    ]
    response = '<br>'.join(response)
    return response

if __name__=="__main__":
    app.run(debug=True)
