# mengimport math dalam pi untuk mendapatkan rumu pi 3.14
from math import pi


class hitungluas:
    def __init__(self,r):
        self.r = r  
    
    # return self.r nya  / bisa di kirim ke html
    def output_luas(self):
        return self.r

    # function yang akan di kirim ke html hasil_luas.html 
    def luas(self):
        return pi * self.r * self.r


###############################################################################################################

class hitungkeliling:
    def __init__(self,l):
        self.l = l 
    
    # return self.l nya
    def output_keliling(self):
        return self.l 
    
    # function yang akan di kirim ke html hasil_lebar.html
    def lebar(self):
        return pi * self.l ** 2

