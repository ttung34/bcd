a = int(input("nhap vao so a "))
b = int(input("nhap vao so b "))
c = int(input("nhap vao so c "))
delta = b**2-4*a*c
if delta>0:
    print("phuong trinh co 2 nghiem x1,x2: ")
elif delta == 0:
    print("phuong trinh co nghiem kep", x=(-b/2*a))
else:
    print("phuong trinh vo nghiem")