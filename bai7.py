class GiaoDich:
    def __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong):
        self.ma_giao_dich = ma_giao_dich
        self.ngay_giao_dich = ngay_giao_dich
        self.don_gia = don_gia
        self.so_luong = so_luong

    def tinh_thanh_tien(self):
        return self.so_luong * self.don_gia

class GiaoDichvang(GiaoDich):
    def  __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong , loai):
        super().__init__(ma_giao_dich, ngay_giao_dich, don_gia, so_luong)
        self.loai = loai
    
    def tinh_thanh_tien(self):
        return super().tinh_thanh_tien()
    
class GiaoDichtiente(GiaoDich):
    def __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong,loai):
        super().__init__(ma_giao_dich, ngay_giao_dich, don_gia, so_luong)
        self.loai = loai
    def mua(self):
        return super().tinh_thanh_tien()
    def ban(self):
        return self.mua()*1.05
    
vang24k = GiaoDichvang("321021","12/4/2004",2000,12,"24k")
vang18k = GiaoDichvang("211021","3/12/2007",2020,13,"18k")
vang9999 = GiaoDichvang("333321","1/8/2001",2000,5,"9999")
vang24k1 = GiaoDichvang("121021","23/5/2003",4500,8,"24k")
vang18k2 = GiaoDichvang("233111","4/4/2005",2500,7,"18k")


dsvang = [vang24k,vang18k,vang9999,vang24k1,vang18k2]

slvang24 = 0
slvang18 = 0
slvang9999 = 0
for i in dsvang:
    if i.loai == "24k":
        slvang24+= i.so_luong
    if i.loai == "18k":
        slvang18+= i.so_luong    
    if i.loai == "9999":
        slvang9999+= i.so_luong

print("so luong loai vang 24K : ",slvang24)
print("so luong loai vang 18K : ",slvang18)
print("so luong loai vang 9999K : ",slvang9999)