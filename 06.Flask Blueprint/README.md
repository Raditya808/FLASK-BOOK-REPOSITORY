# Blueprint Syntax

<p>Pemanggilan file ke file menggunakan Syntax Bluprints di file baru untuk variabel dan app.register di file untuk jalankan file Utama di variabel itu dan menggunakan
from file to varibel Blueprint
</p>



## Code 

```bash 
-file run.py 
# membuat library flasl dengan url_for untuk tombol
from flask import Flask,redirect, url_for

# mengimport file test1.py dan isi Blueprint nya agar bisa di panggil lewatt url_for 
from test1 import TES1

from test2 import TES2


# package flask untuk route 
app = Flask(__name__)

# Blueprint dari test1.py bernama TES1
app.register_blueprint(TES1)

app.register_blueprint(TES2)


@app.route('/')
def run_index():
    return f"""Ini rute run.py
            <h1>Halo dari run.py</h1>
            <!-- Membuat tombol ke arah test1.py mulai dari isi Blueprint dari TES1 bernama ts1 lalu menggunakan titik dan memanggil function nya bernama index_tes1-->
            <a href="{url_for('ts1.index_tes1')}">tes1</a>
            <a href="{url_for('ts2.index_tes2')}">tes2</a>
            """

if __name__=="__main__":
    app.run(debug=True)

```


```bash
- test1.py
# library Blueprint untuk flask menggunakan url for dan Flask 
from flask import Blueprint, Flask, url_for

# membuat Blueprint bernama TES1 yang akan di kirim ke run.py melalui from test1 import TES1
TES1 = Blueprint('ts1',__name__)


@TES1.route('/tes1')
def index_tes1():
    return f"""ini rute test1.py
        <h1>Halo dari rute test1.py</h1>
        <a href={url_for('run_index')}>run.py</a>
        <a href="{url_for('ts2.index_tes2')}">tes2.py</a>
        """
```


```bash
- tes2.py
from flask import Flask,Blueprint,url_for

TES2 = Blueprint('ts2',__name__)

@TES2.route('/tes2')
def index_tes2():
    return f"""ini rute test2.py
    <h1>Halo dari rute test2.py</h1>
    <a href="{url_for('run_index')}">run.py</a>
    <a href="{url_for('ts1.index_tes1')}">tes1.py</a>
    """
```
