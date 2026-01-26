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
