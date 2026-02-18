import sqlite3

conn = sqlite3.connect('newtes.db')

cursor = conn.cursor()

cursor.execute('CREATE TABLE daftarkehadiran (nomor INT NOT NULL, nama VARCHAR(20) , kehadiran VARCHAR(10), PRIMARY KEY(nomor))')


###########################################################################################################
# data 1                                                                                ###################
cursor.execute('INSERT INTO daftarkehadiran VALUES(1,"radit","hadir")')                 ###################
                                                                                        ###################
# data 2 adding ur own if u wanna changes datas just use cursor.                        ################### execute                                                                                 ###################
                                                                                        ###################
                                                                                        ###################
###########################################################################################################

# conn commit berfungsi untuk menyimpan perubahan yang telah dilakukan pada database
conn.commit()
# conn.commit() dan cursor.close() berfungsi untuk menutup koneksi ke database
conn.cursor()
# conn.close() berfungsi untuk menutup koneksi ke database
conn.close()
# cursor berfungsi untuk menutup cursor
cursor.close()
