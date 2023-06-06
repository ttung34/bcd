#Vòng lặp for lồng nhau
name = "thanhtung"
for i in range(0, 10):
    for j in range(i,10):
        print(j, end = " ")
    print("")
    
#i là các biên tạm dùng để chứa dữ liệu sau mỗi lần lặp
#name là một list, tuple hoặc string,... chứa giá trị cần lặp


#Vòng lặp while lồng 2 vòng
i = 1
while(i<10):
    j = 1
    while(j<= 10-i):
        print(j, end = " ")
        j += 1
    print("")
    i += 1