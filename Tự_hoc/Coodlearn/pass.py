class Perrson:
  def __init__(self, name, age):
        self.name = name
        self.age =age

  def info(self):
      print(self.name + ",", self.age, "years old.")
#Sinh viên thừa kế từ người
#Mà không thêm bất lỳ thuộc tinh hoặc phương thucws   
      
class Student(Perrson):
    pass

hs = Student("ThanhTung", 18)
hs.info()