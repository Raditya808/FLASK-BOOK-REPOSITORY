from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    a = 10 
    b = 5 
    return render_template('jinja.html',a=a,b=b)

# untuk mengetikan kondisi jinja 
# diawali dengan menggunakan {} kurawal dan didalam kurawal di ketik menggunakan %% 
# {%if kondisi%}
# {%endif%} untuk menutup kondisi
# kode diatas dikirim lewat html
# kondisi ini bisa menggunakan or and || &&

if __name__ =="__main__":
    app.run(debug=True)
