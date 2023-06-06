num1 = int(input()) 
num2 = int(input())

if num1 >= num2:
    if num1 == num2:
        print(num1, 'và', num2, 'bằng nhau')
        print("Tích của",num1,"và",num2,"là:",num1*num2)  
    else:
        print(num1, 'lớn hơn', num2)
        print("Hiệu của", num1,"và",num2,"là:",num1-num2)
else:
    print(num1, 'is smaller than', num2)
    print("Tổng của",num1,"và",num2,"là:",num1+num2)