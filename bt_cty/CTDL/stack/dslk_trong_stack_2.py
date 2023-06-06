from dslk_trong_stack import DSLienKet

class HangDoi:
    #Queue
    def __init__(self):
        self.danh_sach =DSLienKet()
        
    def __str__(self):
        kq = "Hang Doi ["
        kq =kq+str(self.danh_sach)
        kq =kq+"]"
        return kq
        
    def la_rong(self):
        return self.danh_sach.dau == None
    
    def xep_hang(self, gia_tri):
        #enqueue
        self.danh_sach.them_duoi(gia_tri)
        
    def lay_ra(self):
        #dequeue
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()
            return kq
        
if __name__ == "__main__":
    hang_doi = HangDoi()
    print(hang_doi)
    
    print("*** Xep Hang ***")
    for i in range(1,11):
        print(f"*Xep hang gia tri {i}")
        hang_doi.xep_hang(i)
        print(hang_doi)
        
    print("*** Lay ra ***")
    while not hang_doi.la_rong():
        print(f"*** Lay Ra ***")
        gt = hang_doi.lay_ra()
        print(f"Lay ra -> {gt}")
        print(hang_doi)
        
        