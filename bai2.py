import math
class tamgiac:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def chuvi(self):
        x = self.a+self.b+self.c
        print("Chu Vi: ",x)
    def dientich(self):
        x = self.a+self.b+self.c
        x = x / 2
        s = math.sqrt(x*(x-self.a)*(x-self.b)*(x-self.c))
        print("dien tich: ",s)
    def loai(self):
        x = self.a
        y = self.b
        z = self.c
        if x == y and x == z:
            print("Tam giac deu")
            return
        l = [x,y,z]
        l.sort()
        if (x == y or x == z or z == y):
            if l[2]**2 == l[1]**2 +l[0]**2:
                print("tam giac vuong can")
                return
            else:
                print("tam giac can")
                return
        else:
            if l[2]**2 == l[1]**2 +l[0]**2:
                print("tam giac vuong")
                return 
            print("tam giac thuong")
    def intt(self):
        print("co 3 canh lan luot la : ",self.a,self.b,self.c)
        print("mau ",self.d)
        self.chuvi()
        self.dientich()
        self.loai()


a = tamgiac(3,4,5,"cam")
a.intt()