from flask import Flask,render_template,request
from classtes import User  

app =Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    models = User() 
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        
        # models.setUsername adalah objek function yang ada di classtes.py
        models.setUsername(username)
        # models.setUsername adalah objek function yang ada di classtes.py
        models.setPassword(password)

        # models dari variabel diatas authenticate adalah dari class function bernama authenticate
        if models.authenticate():
            return render_template('login_success.html',models=models)
        else:
            return render_template('error.html')
        
    else:
        return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)
