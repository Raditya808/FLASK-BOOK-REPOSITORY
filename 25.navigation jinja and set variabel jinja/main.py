from flask import Flask,render_template


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/second_route')
def sec_route():
    return f'''
    <h1>Welcome to sec route</h1>

    '''
@app.route('/third_route')
def thrd_route():
    return f"""
    <h1>Welcme to thrd route</h1>
"""

if __name__=="__main__":
    app.run(debug=True)
