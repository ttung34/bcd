class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def info(self):
    print(self.name + ",", self.age, "years old.")

# create objects of Person class
thanhtung = Person("thaonguyen", 18)
thanhtung.info()
thaonguyen = Person("thanhtung", 18)
thaonguyen.info()
