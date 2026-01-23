<div align="center"><img src="https://raw.githubusercontent.com/pallets/flask/refs/heads/stable/docs/_static/flask-name.svg" alt="" height="150"></div>

# Flask

Flask is a lightweight [WSGI] web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around [Werkzeug]
and [Jinja], and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

[WSGI]: https://wsgi.readthedocs.io/
[Werkzeug]: https://werkzeug.palletsprojects.com/
[Jinja]: https://jinja.palletsprojects.com/

## A Simple Example

```python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Donate

The Pallets organization develops and supports Flask and the libraries
it uses. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today].

[please donate today]: https://palletsprojects.com/donate

## Contributing

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/

# WSGI GET 


<p>ROUTING LOCALHOST</p>

<p>Cara Kerja slash / di rute web FLASK</p>



## Code 


```bash 

from flask import Flask

application = Flask(__name__)


# rute yang tidak ada parameter
# langsung di arahkan rute web pertama
@application.route('/')
def index():
    return f"hello from flask"

# rute dengan name 
# memanggil hasil menggunakan %
# /hello/radit
@application.route('/hello/<name>')
def index2(name):
    return f"<h1>Halo %s</h1>" % name

# rute dengan integer 
# /number/5 
@application.route('/number/<angka>')
def index3(angka):
    return f"<h1>Page %s</h1>" %angka



if __name__=="__main__":
 
```
