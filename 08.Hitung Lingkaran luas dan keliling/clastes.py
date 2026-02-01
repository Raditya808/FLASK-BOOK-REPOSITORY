from math import pi 

class lingkaran:
    def __init__(self):
        self.radius = 0 

    def set_radius(self,r):
        self.radius = r 

    def get_radius(self):
        return self.radius

    def hitungluas(self):
        return pi * (self.radius **2)

    def hitungkeliling(self):
        return 2 * pi * self.radius
