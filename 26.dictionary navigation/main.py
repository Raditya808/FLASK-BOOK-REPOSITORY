from flask import Flask,render_template



app = Flask(__name__)



# send to nav html
@app.route('/')
def route():
    # dictionary to store navigation
    dict_nav = {
        '/':'home',
        '/route2':'route2',
        '/route3':'route3'
}
    return render_template('nav.html',dict_nav=dict_nav)


@app.route('/route2')
def route2():
    return f'''
    <p>route 2 path</p>
    '''

@app.route('/route3')
def route3():
    return f'''
    <p>route 3 path </p>
    '''

if __name__ =="__main__":
    app.run(debug=True)
