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
