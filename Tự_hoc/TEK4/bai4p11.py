#Hãy viết chương trình thêm phần tử 7000 vào sau 
# phần tử 6000 thuộc danh sách con bên trong của 
# danh sách đã cho và sau đó in danh sách sau khi 
# đã được thêm ra màn hình.
a = [10,20,[300,400,[5000,6000],500],30,40]
b =a[2][2]
b.append(7000)
print(a)