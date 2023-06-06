a = int(input("nhap vao so a "))
b = int(input("nhap vao so b "))
c = int(input("nhap vao so c "))
if a**2+b**2==c**2:
        print("la tam giac vuong")
elif a==b==c:
        print("la tam giac deu")
elif (a==b) and (b==c) and (c==a):
        print("la tam giac can")
elif (a**2>b**2+c**2) and (a*a+b*b<c*c) and(b*b>a*a+c*c):
        print("là tam giac tu")
else:
    print("la tam giac nhon")