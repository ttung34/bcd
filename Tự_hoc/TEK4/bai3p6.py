#Năm nhuận
a = int(input("nhap nam vao "))
if a %4 ==0:
    if a%100==0 and a%400==0:
        print("năm",a,"không phải năm nhuận")
    else:
        print("năm",a, "la năm nhuận")
else:
    print("năm",a, "không phải là năm nhuận")