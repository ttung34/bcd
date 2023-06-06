#BÀI 3 Kế thừa class trong python
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex =sex
    def Ten(self):
        return self.name
    def Tuoi(self):
        return self.age
    def Sex(self):
        return self.sex 
class Male(Person):
    sex = "Male"
    
male =Male("Thanh Tung",18, "nam")
print(male.Ten())
print(male.Tuoi())
print(male.Sex())    

#Ghi đè
class foo:
    name = "foo"
    def getname(self):
        print("Class: Foo")
class Bar(foo):
    name = "Bar"
    def getname(self):
        print("Class: Bar" + super().name)
        super().name()

Bar().getname()

#Đa kế thừa
class first:
    def getfirst(self):
        print("class first")
class second:
    def getsecond(self):
        print("class second")
class third(first,second):
    def getthird(self):
        print("class third")
        
ba = third()
ba.getfirst()
ba.getsecond()
ba.getthird()
