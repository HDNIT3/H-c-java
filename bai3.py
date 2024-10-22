class ns:
    def __init__(self,*n):
        self.n = n 
    def tinhtong(self):
        return sum(self.n)
    def trungbinh(self):
        return sum(self.n)/len(self.n)
    def min(self):
        m = self.n[0]
        for i in self.n:
            if i < m:
                m = i
        return m
    def max(self):
        m = self.n[0]
        for i in self.n:
            if i > m:
                m = i
        return m
    def tt(self):
        print(f"thông số: ")
        for i in self.n:
            print(i,end=" ")

p = ns(1,3,3,4)

print(f"Tổng là : {p.tinhtong()}")
print(f"Trung bình là : {p.trungbinh()}")
print(f"Min là : {p.min()}")
print(f"Max là : {p.max()}")
p.tt()

    