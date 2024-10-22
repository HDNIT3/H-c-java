import math
class hinh:
    def  __init__(self):
        pass
    def chuvi(self):
        pass
    def dientich(self):
        pass


class hcn(hinh):
    def __init__(self,cd,cr):
        self.cd = cd
        self.cr = cr
    def chuvi(self):
        x = (self.cd+self.cr)*2
        print("chu vi : ",x)
    def dientich(self):
        x = (self.cd*self.cr)
        print("Dien tich : ",x)

class tron(hinh):
    def __init__(self,r):
        self.r = r
    def chuvi(self):
        x = self.r*math.pi*2
        print("Chu Vi: ",x)
    def dientich(self):
        x = round(math.pi*self.r**2,2)
        print("Dien tich : ",x)

class tamgiac(hinh):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def chuvi(self):
        x = self.a+self.b+self.c
        print("Chu Vi: ",x)
    def dientich(self):
        x = self.a+self.b+self.c
        x = x / 2
        s = math.sqrt(x*(x-self.a)*(x-self.b)*(x-self.c))
        print("dien tich: ",s)

a = tron(2)
print("----Hình Tròn: ---")
a.chuvi()
a.dientich()

b = hcn(2,4)
print("---Hình CN: ---" )
b.chuvi()
b.dientich()

c = tamgiac(3,4,5)
print("--- Hình Tam giac : ---")
c.chuvi()
c.dientich()