from danh_sach_lien_ket_liked import *

def main():
    ds = DSLienKet()
    ds.in_ds()
    
    #a-them
    print("a - Them")
    so = 34
    print(f"Them {so}")
    ds.them(so)
    ds.in_ds()
    
    so = 11
    print(f"Them {so}")
    ds.them(so)
    ds.in_ds()
    
    #b-chen
    print("b: chen them so vao danh sach")
    so = 9
    vitri = 0
    print(f"Chen so {so} vao vi tri {vitri}")
    ds.chen(vitri,so)
    ds.in_ds()
    
    so = 6
    vitri = 2
    print(f"Chen so {so} vao vi tri {vitri}")
    ds.chen(vitri,so)
    ds.in_ds()
    
    so = 20
    vitri = 5
    print(f"Chen so {so} vao vi tri {vitri}")
    ds.chen(vitri,so)
    ds.in_ds()
    
    #c-tim
    print("C tim vi tri trong bang")
    ds.in_ds()
    so = 99
    print(f"Tim {so}")
    vitri = ds.tim(so)
    print(f"So {so} tai vi tri {vitri}")
    
    print("C tim vi tri trong bang")
    ds.in_ds()
    so = 20
    print(f"Tim {so}")
    vitri = ds.tim(so)
    print(f"So {so} tai vi tri {vitri}")
    
    #d-xoa
    print("D: Xoa phan tu trong bang")
    so = 19
    print(f"Xoa so {so}")
    ds.xoa(so)
    ds.in_ds()
    
    print("D: Xoa phan tu trong bang")
    so = 15
    print(f"Xoa so {so}")
    ds.xoa(so)
    ds.in_ds()
    
    #e-cap nhap
    print("E: CAP NHAT VI TRI MOI CUA BANG")
    vitri = 6
    gia_tri = 24
    print(f"Cap nha {vitri} voi gia tri {gia_tri}")
    ds.cap_nhat(vitri, gia_tri)
    ds.in_ds()
    
    print("E: CAP NHAT VI TRI MOI CUA BANG")
    vitri = 3
    gia_tri = 225
    print(f"Cap nha {vitri} voi gia tri {gia_tri}")
    ds.cap_nhat(vitri, gia_tri)
    ds.in_ds()
    
    #f-xoa het
    print("F: XOA HET CAC GIA TRI CUA BANG")
    print("Xoa het")
    ds.xoa_het()
    ds.in_ds()

if __name__ == "__main__":
    main()