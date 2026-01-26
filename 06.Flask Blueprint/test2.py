from flask import Flask,Blueprint,url_for

TES2 = Blueprint('ts2',__name__)

@TES2.route('/tes2')
def index_tes2():
    return f"""ini rute test2.py
    <h1>Halo dari rute test2.py</h1>
    <a href="{url_for('run_index')}">run.py</a>
    <a href="{url_for('ts1.index_tes1')}">tes1.py</a>
    """
