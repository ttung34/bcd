import random

def san_sinh_so_ngau_nhien(n):
    mang = []
    
    for i in range(10):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)
        
    return mang

def sap_xep_chen(mang):
    for i in range(1,len(mang)):
        tam = mang[i]
        j=i 
        
        while j>0 and mang[j-1]>tam:
            mang[j]=mang[j-1]
            j-=1
        
        mang[j] = tam
        print(i,' ',mang) 
mang= san_sinh_so_ngau_nhien(10)
print(f"mang ban dau la {mang}")
sap_xep_chen(mang)
print(f"Mang sau khi sap la {mang}")  