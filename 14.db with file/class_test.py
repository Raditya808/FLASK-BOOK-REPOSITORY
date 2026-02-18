import os 
import sqlite3


# database locaction
databasefile = os.getcwd() + '/newtes.db'

class daftarkehadiran:
    def __init__(self,nomor,nama,absen):
        self.nomor = nomor 
        self.nama = nama
        self.absen = absen

    
    # fitur tambah
    def tambah(self):
        conn = sqlite3.connect(databasefile)
        cursor = conn.cursor()
        conn.execute('SELECT * FROM daftarkehadiran')
        conn.commit()
        cursor.close()
        conn.close()
