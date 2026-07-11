from flask import Flask,render_template, request

app = Flask(__name__)


# route for '/'
# make variabel and send to html template
@app.route('/',methods=['GET','POST'])
def navigation_jinja():
    if request.method == 'POST':
    # var with request form to send html  
        # var with name a and send as request.form to html else condition and send to name="" attribute
        a =  int(request.form['number_input'])
        return render_template('navigation.html',a=a)
    
    else:
        return f"""
        <!DOCTYPE html> 
        <html>
            <head>
                <title>Form_input</title>
            </head>
            <body>
                <h1>iNPT</h1>
                <div class="session_form">
                    <!-- send post condition and name attribute from request.form-->
                    <form method="POST">
                        <input type="number" name="number_input" placeholder="choose the num">
                        <input type="submit" value="kirim"> 
                    </form>
                </div>
            </body>
        </html>
        
    """

    app.run(debug=True)


if __name__ =="__main__":
    app.run(debug=True)
