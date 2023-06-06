class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
        
  def info(self):
    print(self.name + ",", self.age, "years old.")
        
#Sinh viên kế thừa người:       
class Student(person):
  def __init__(self, name, age, id):
    super().__init__(name, age) #hàm super giúp lớp con tự động kế thừa các thuộc tính và phương thức từ lớp cha
    self.id = id 
    
  def infoStudent(self):
    print(self.name + ",", self.age, "years old,  id:",self.id) 
        
son = Student("Son", 18, "0368033203")
son.infoStudent() 
    