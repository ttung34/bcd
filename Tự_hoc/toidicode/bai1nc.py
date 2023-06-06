#Class và cách khai báo class trong python
class Person:
    #thuộc tính
    name = "ThanhTung"
    age = 18
    male = True
    #phương thức
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age 
    def setMale(self, male):
        self.male = male   
    def getMale(self):
        return self.male


#khởi tạo class
T = Person()
print(Person.name)
print(Person.age)
print(Person.male)
#truy cập đến thuộc tính 

#truy cập đến phương thức
T.setName("Thao Nguyen")
print(T.getName())
T.setAge(18)
print(T.getAge())
