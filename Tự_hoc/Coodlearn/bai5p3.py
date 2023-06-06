a = int(input("nhap vao so a "))
b = int(input("nhap vao so b "))
c = int(input("nhap vao so c "))
avg = (a + b +c)/3
if avg > a and avg >b:
    print("The average value is greater than both a and b")
if avg > a and avg >c:
    print("The average value is greater than both a and c")    
if avg > b and avg >c:
    print("The average value is greater than both b and c")
elif avg > a:
    print("The average value is greater than a")
elif avg > b:
    print("The average value is greater than b")
else:
    print("The average value is greater than c")