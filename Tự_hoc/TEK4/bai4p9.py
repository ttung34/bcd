#Một số thao tác cơ bản trên danh sách trong python
#Thay dổi các phần tử trong danh sách
a = [50,100,200,300,400]
print(a)
a[4]=500
print(a)
a[1:4]=[400,50,30]
print(a)
#thêm phần tử vào vị trí cuối cùng
a.append(900)
print(a)
#thêm một phần tử vào vị trí bất kỳ
a.insert(6,600)#đứng trước là vị trí chèn, đứng sau là giá trị cần chèn
print(a)
#thêm nhiều phần tử vào cuối danh sách
a.extend([3,5,7])
print(a)
#Xóa các phần tử khỏi danh sách
my_list = list([1,2,3,4,5,6,7])
my_list.remove(5)
my_list.remove(7)
print(my_list)
#Xóa phần tử ở vị trí được chỉ đingj trong list
my_list.pop(2)
print(my_list)
my_list.pop()#Xóa phần tử cuối cùng khi pop để trống
print(my_list)
#Xóa nhiều phần tử trong danh sách
del my_list[0:1]
print(my_list)
b = list([4,5,6,7,8,9])
del b[3:]
print(b)
b.clear()
print(b)