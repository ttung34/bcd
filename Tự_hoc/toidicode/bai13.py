#2 Đọc ghi file
#MỞ FILE: để mở file trong python chúng 
# ta sử dụng hàm open với cú pháp (open(filePath, mode, buffer))
#ĐÓNG FILE: fileObject.close()
#fileObject là đối tượng mà chúng ta thu được khi sử dụng hàm open()
#ĐỌC FILE:Sau khi mở file ra rồi, để đọc được file thì chúng ta sử dụng phương thức read với cú pháp fileObject.read(length)
#fileObject là đối tượng mà chúng ta thu được khi sử dụng hàm open()
#length là dung lượng của dữ liệu mà chúng ta muốn đọc, nếu file để trống tham số này nó sẽ đọc hết file hoặc nếu file lớn quá thì nó sẽ đọc đến khi giới hạn của bộ nhớ cho phép
#GHI FILE: 
file = open("thu.py", "w")
print(file.name)