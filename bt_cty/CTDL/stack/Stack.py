class NganXep:
    def __init__(self):
        self.danh_sach = []
        
        
    def la_rong(self):
        return len(self.danh_sach) == 0
    
    def __str__(self):#Chuyen ngan xep ve kieu chuoi
        kq = 'Ngan xep ['
        stt = 0
        for x in self.danh_sach:
            stt +=1
            if stt == 1:
                kq=kq + str(x)
            else:
                kq  = kq +"->"+str(x)
                
        kq =kq+']'
        return kq
    
    def day_vao(self,gia_tri):
        self.danh_sach.append( gia_tri)
        
    def lay_ra(self):
        if self.la_rong():
            return None
        else:
            return self.danh_sach.pop()
        
if __name__ == "__main__":
    ngan_xep = NganXep()
    print(ngan_xep)
    
    
    print("----- Day vao-----")
    for i in range(1,6):
        print(f"*** Day vao {i}")
        ngan_xep.day_vao(i) 
        print(ngan_xep)       
        
    print("***** Lay Ra *****")
    while not ngan_xep.la_rong():
        gt =ngan_xep.lay_ra()
        print(f"**Lay ra ->{gt}")
        print(ngan_xep)