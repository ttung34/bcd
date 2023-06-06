class Nut:
    def __init__(self,khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
    #def

    def chen(self,khoa):
        if self  is None:
            nut = Nut(khoa)
            self = nut
            return
        #if         
        if khoa<self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa)
            else:
                self.trai.chen(khoa)
            #if
        elif khoa >self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
                self.phai.chen(khoa)
        else:
            print(f"Khoa bi trung khoa {khoa}")
        #if
    #def
#class

class CayNhiPhanTimKiem:
    def __init__(self,khoa=None):
        if khoa == None:
            self.goc = None
        else:
            self.goc = Nut(khoa)
            # print(Nut(khoa))
        #if         
    #def
    
    def chen(self,khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else:
            self.goc.chen(khoa)     
        #if
    #def
    
    def xoa(self, khoa):
        nut_cha = None                 
        cha_con = None
        nut_ht = self.goc
        
        while nut_ht != None:
            if nut_ht.khoa>khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.trai
                cha_con = "trai"
            elif nut_ht.khoa<khoa:
                nut_cha = nut_ht
                nut_ht=nut_ht.phai
                cha_con = "phai"
            else:# Tim thay nut
                if nut_cha == None:
                    #Xoa nut goc
                    if nut_ht.trai == None and nut_ht.phai == None:
                        #Xoa nut goc khong co con
                        self.goc = None
                    elif nut_ht.trai == None:
                        #Xoa nut goc chi co mot nut con ben phai
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        #Xoa cai nut goc chi co mot nut con ben trai
                        self.goc = nut_ht.trai
                    else:
                        #Xoa nut goc co du hai con
                        #Xoay ve ben trai
                        self.goc = nut_ht.phai
                        tam = self.goc
                        while tam.trai != None:
                            tam = tam.trai
                        #while
                        tam.trai = nut_ht.trai
                    #if                
                elif nut_ht.trai == None and nut_ht.phai == None:
                    #Xoa nut las
                    if cha_con == 'trai':
                         nut_cha.trai = None
                    else:
                        nut_cha.phai = None
                    #if
                elif nut_ht.trai==None:
                    #Xoa nut chi co mot con ben phai
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    #if
                elif nut_ht.phai == None:
                    #Xoa nut chi co mot con ben trai
                    if cha_con =='trai':
                        nut_cha.trai = nut_ht.trai
                    else:
                        nut_cha.phai=nut_ht.trai
                    #if
                else:
                    #Xoa nut co du hai con
                    #Xoa trai
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    #if
                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai
                    else:
                        tam = nut_ht.phai
                        while tam.trai != None:
                            tam = tam.trai
                        #while
                        tam.trai = nut_ht.trai
                    #if             
                #if   
            del nut_ht
            break
            #if
        #while    
    #def
    
    def duyet_trai_nut_phai(self, goc=0):
        #duyet theo LNR
        
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        if nut_ht == None:
            return []
        else:
            kq =[]
            
            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)#Goi de quy truyen cho no nut hien tai ow 
            #ben trai de lay tat ca phan tu nam phia ben tay trai
            for x in kq_trai:
                kq.append(x)
            #for
            kq.append(nut_ht.khoa)
            
            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for   
            
            return kq
        #if   
    #def
    
    def duyet_nut_trai_phai(self,goc=0):
        # Duyet theo NLR
        
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        if nut_ht == None:
            return []
        else:
            kq =[]
            
            kq.append(nut_ht.khoa)
            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)#Goi de quy truyen cho no nut hien tai ow 
            #ben trai de lay tat ca phan tu nam phia ben tay trai
            for x in kq_trai:
                kq.append(x)
            #for
            
            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for   
            
            return kq   
    #def
    
    def duyet_trai_phai_nut(self, goc=0):
        # Duyet theo LRN
        
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        if nut_ht == None:
            return []
        else:
            kq =[]
            
            kq_trai = self.duyet_trai_phai_nut(nut_ht.trai)#Goi de quy truyen cho no nut hien tai ow 
            #ben trai de lay tat ca phan tu nam phia ben tay trai
            for x in kq_trai:
                kq.append(x)
            #for
            
            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for  
            
            kq.append(nut_ht.khoa) 
            
            return kq
    #def
    
    def tim(self,khoa):
        if self.goc == None:
            return
        #if
        
        nut_ht = self.goc
        kq = ''
        while (nut_ht != None and nut_ht,khoa != khoa):
            kq = kq+ f'{nut_ht.khoa} ->'
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai
            #if
        #while
        
        if nut_ht == None:
            return None
        else:
            kq = kq + f'{nut_ht.khoa}'
            return kq
        #if
    #def
#class

def main():
    So_phan_tu = 10
    
    cay = CayNhiPhanTimKiem()
    
    print("**** Chen vao cay ****")
    tap_gia_tri = set()
    from random import randint
    while len(tap_gia_tri)<So_phan_tu:
        gt = randint(1,100)
        tap_gia_tri.add(gt)
    #while
    
    tap_gia_tri = list(tap_gia_tri)
    tap_gia_tri  = [66,46,84,11,81,99,36,77,83,87,100,86,85]
    
    print(f"Chen lan luot {tap_gia_tri}") 
    for x in tap_gia_tri:
        cay.chen(x)
    #for
    
    kq = cay.duyet_trai_nut_phai()
    print(f"*** Duyet cay theo trai nut phai (LNR): {kq}")
    
    kq = cay.duyet_nut_trai_phai()
    print(f"*** Duyet cay theo nut trai phai (NLR): {kq}")
    
    kq = cay.duyet_trai_phai_nut()
    print(f"*** Duyet cay theo trai phai nut LRN: {kq}")    

    gt = input("Nhap so can xoa: ")
    print(f"Xoa {gt}")
    cay.xoa(gt)

    while True:
        nhap = input("Nhap vao khoa can tim: ")
        if nhap == " ":
            break
        #if
        
        gt = int(nhap)
        kq = cay.tim(gt)
        if kq == None:
            print(f"Khong tim thay gia tri khoa: {gt}")
        else:
            print(f"Tim thay {gt} : {kq}")
        #if
    #while    
#def

if __name__ == "__main__":
    main()
#if
