class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def info(self):
    print(self.name + ",", self.age, "years old.")

# Student inherits from Person
class Student(Person):
  def __init__(self, name, age):
    super().__init__(name, age)
    
son = Student("thanhtung", 18)
son.info()