#Hàm là gì ? hàm là một tập các khối code đuọc viết ra nhắm cho việc tái dử dụng code
#2 Khai báo hàm trong python
def sum(a, b):
    print("sum ="+str(a+b))
sum(3,4)
#4 Hàm có kết quả trả về
#trong trường hợp bạn muốn sử dụng kết quả của hàm vừa tính để thực hiện các mục đích khác.Thì chỉ cần thêm return trước kết quả bạn muốn trả về
def sun(a, b):
    return a+b



c  = sun(3, 4);
print("tong"+ str(c))

#7 Biến global biến toàn cầu, khi một biến là global thì chúng ta có thể gọi và tác động đến nó từ bất kỳ đâu trong chương trình
#Để khai báo một biến là global thì chúng ta chỉ cần thêm global trước tên của nó
a = "thanhtung"
def say():
    global a
    a = "thaonguyen" 
    print(a)
say()
print(a)   
#8 truyền vô số tham số vào hàm
def sim(*num): # python cũng cấp cho chúng ta khai báo một param đại diện cho các biến truyền vào hàm bằng cách thêm dấu * vào trước param đó
    tmp = 0
    for i in num:
        tmp += i
    return tmp

result = sim(1,2,3,4,5)


print(result)
