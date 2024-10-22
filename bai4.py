
class diem:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
    def intt(self):
        print(f"Điểm có tọa độ x = {self.x} và y = {self.y}")

        
    def tinhtien(self,x,y = None):
        self.x = self.x + int(x)
        if y is None:
            print(f"Sau khi tinh tien x có tọa độ x = {self.x} và y = {self.y}")
        else:
            self.y = self.y + int(y)
            print(f"Sau khi tinh tien x và y có tọa độ x = {self.x} và y = {self.y}")

    def khoangcach(self,c = None):
        if c is None:
            ff = ((self.x)**2+(self.y)**2)**0.5
            print(f"Khoảng cách điểm với tọa độ 0 là : {ff}")
        else:  
            ff = ((self.x-c.x)**2+(self.y-c.y)**2)**0.5  
            print(f"Khoảng cách giữa 2 điểm là : {ff}")
    
a = diem(3,4)
a.intt()
a.tinhtien(2)
a.tinhtien(3,2)
a.khoangcach()
a.khoangcach(c = diem(1,2))
    


