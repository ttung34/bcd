i = input("nhap vao so i ")
a = [-1.2,48,4.6,56,5,56.9,98,99,18,9.9]
b = len(a)
if i in range(0,b-1) and i in range (-b,1):
    
    print("phan tu thu",i,"tu cuoi len có gia tri la: ",a[i])
else:
    print(i,"list index out of range")