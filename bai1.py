import math
class tron:
    def __init__(self,r):
        self.r = r
    def chuvi(self):
        x = self.r*math.pi*2
        print("Co chu vi la: ",x)
    def dientich(self):
        x = round(math.pi*self.r**2,2)
        print("Co dien tich la",x)
    def inthongtin(self):
        print("ban kinh: ",self.r)
        self.chuvi()
        self.dientich()

a = tron(2)

a.inthongtin()