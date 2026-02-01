# mengimport class sqlite3 dan os 
import sqlite3, os 


DATABASE = os.getcwd() + '/dbtest.db'



# di dalam dbtest.db dan di file sql how to create 
# kita membuat db yang isinya kode nama dan harga
# dengan nama db bernama dbtest.db
# kode nama harga di stel saat pembuatan db di import sql di python 
# kode INETEGER NOT NULL, nama adalah VARCHAR(25), harga FLOAT,PRIMARY KEY(kode))
# INTTEGER NOT NULL artinya kode tidak boleh kosong 
# VARCHAR(25) artinya nama maksimal 25 karakter
# FLOAT artinya harga adalah bilangan desimal
# PRIMARY KEY(kode) artinya kode adalah primary key
class produk:
    def __init__(self,kode=0, nama='',harga=0):
        self.kode = kode 
        self.nama = nama 
        self.harga = harga

    # nilai kode di dalam parameter __init__
    # dan membuat parameter kode 
    def setkode(self,kode):
       self.kode = kode  


    # nilai nama di dalam parameter __init__
    # dan membuat parameter nama
    def setnama(self,nama):
        self.nama = nama 

    # nilai harga yang di stel  
    # dan membuat parameter harga
    def setharga(self,harga):
        self.harga = harga


    

    
    # proses nambah data ke database
    # tambah data
    def tambah(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produk VALUES (?,?,?)',(self.kode,self.nama,self.harga))
        conn.commit()
        cursor.close()
        conn.close()


    # ubah menerima satu komponen dari load database nya 
    # komponen edit kode harga dan produk 
    def ubah(self):
        conn = sqlite3.connect(DATABASE) 
        cursor = conn.cursor()
        cursor.execute('''UPDATE produk SET nama=?,harga=? WHERE kode=?''',
        (self.nama,self.harga,self.kode))
        conn.commit()
        cursor.close()
        conn.close()



    # load isi database 
    # load file database
    # SELECT * FROM tabel isi di dbtest.db didalam file bernama table produk
    def load(self,id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        for kode,nama,harga in cursor.execute("SELECT * FROM produk"):
            if kode ==id:
                self.kode = kode 
                self.nama = nama 
                self.harga = harga
                break 
