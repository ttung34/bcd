#định nghĩa một lớp hcn
#Thước tính : chieu dài, chiue rong
#phương thức: tính chu vi, tính diện tích
class HCN:
    chieu_rong = ""
    chieu_dai = ""
    
    def tinhtoan(self):
        
        print("chu_vi: ",(self.chieu_rong+self.chieu_dai)*2)
        print("dien_tich ",(self.chieu_dai*self.chieu_rong))
hcn_1 = HCN()
hcn_1.chieu_dai=15
hcn_1.chieu_rong=9

hcn_2 = HCN()
hcn_2.chieu_dai=20
hcn_2.chieu_rong=4

hcn_1.tinhtoan()
hcn_2.tinhtoan()       