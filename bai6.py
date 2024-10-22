import os
class sinhvien:
    def __init__(self,cccd,ht,nam,dsmon,tiet):
        self.cccd = cccd
        self.ht = ht
        self.nam = nam
        self.dsmon = dsmon
        self.tiet = tiet
    def intt(self):
        print("CCCD: ",self.cccd)
        print("Ho va ten: ",self.ht)
        print("Nam: ",self.nam)
        print("Danh sach mon: ",self.dsmon)
        print("So tiet: ",self.tiet)
        print("----************************-----")
a = []
i = 0 
with open("dssv.txt","r") as f:
    for line in f:
        line = line.rstrip()
        arr = list(line.split(" ; "))
        ss = sinhvien(int(arr[0]),arr[1],int(arr[2]),arr[3],int(arr[4]))
        a.append(ss)

while(True):
    print("0.Thoat")
    print("1.để xem danh sách")      
    print("2.Hiển thị thông tin của các học viên đăng ký ít nhất hai môn học tại trung tâm")      
    print("3.Hiển thị thông tin môn học được nhiều sinh viên đăng ký nhất")      
    print("4.Thống kê số lượng học viên trên môn")      

    c = str(input())
    
    if c == "0":
        os.system("cls")
        print("thoát")
        break
    if c == "1":
        os.system("cls")
        for i in a:
            i.intt() 
        input("enter để thoát")
        os.system("cls")
    if c == "2":
        os.system("cls")
        for i in a:
            lo = i.dsmon.split(",")
            if len(lo) >= 2:
                i.intt()
        input("enter để thoát")
        os.system("cls")
    if c == "3":
        so = {"toan":0,"hoa":0,"ly":0,"van":0,"su":0,"dia":0,"anh":0,"sinh":0,"tin":0}
        os.system("cls")
        for i in a:
            lo = i.dsmon.split(",")
            for d in lo:
               so[d]+=1
        max = 0
        opw = ""
        for i,j in so.items():
            if j > max:
                max = j
                opw = i
        print(opw," : ",max," lần")
        input("enter để thoát")
        os.system("cls")
    if c == "4":
        so = {"toan":0,"hoa":0,"ly":0,"van":0,"su":0,"dia":0,"anh":0,"sinh":0,"tin":0}
        os.system("cls")
        for i in a:
            lo = i.dsmon.split(",")
            for d in lo:
               so[d]+=1
        for i,j in so.items():
            print(f"Mon {i} có {j} người học")
        input("enter để thoát")
        os.system("cls")
    