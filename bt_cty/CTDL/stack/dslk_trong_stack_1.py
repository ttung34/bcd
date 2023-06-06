from dslk_trong_stack import DSLienKet

class NganXep:
    def __init__(self):
        self.danh_sach = DSLienKet()
        
    def la_rong(self):
        return self.danh_sach.dau == None
    
    def __str__(self):#Phuong thuc bien thanh chuoi
        kq = "Ngan xep ["
        kq = kq + str(self.danh_sach)
        kq = kq +"]"
        return kq
    
    def day_vao(self,gia_tri):
        self.danh_sach.them_dau(gia_tri)
        
    def lay_ra(self):
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()
            return kq
        
if __name__ == "__main__":
    ngan_xep = NganXep()
    print(ngan_xep)
    
    print("**** Day vao ****")
    for i in range(1,6):
        print(f"Day vao gia tri {i}")
        ngan_xep.day_vao(i)
        print(ngan_xep)
        
    print("**** Lay ra ****")
    while not ngan_xep.la_rong():
        gt  = ngan_xep.lay_ra()
        print(f"** Lay ra -> {gt}")
        print(ngan_xep)
        
    
        