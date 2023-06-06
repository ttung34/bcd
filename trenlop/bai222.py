#TÊN: LE VIET HUNG
#LỚP: DCCTCLC67A
#MSV:2221050367

#BÀI 1:
#Object-oriented programming is a programming paradigm based on the concept of "objects". 
#The object contains both data and code: 
#-Data in the form of properties (often known as attributes), and code, in the form of methods (actions object can perform).
#An object has the following two characteristics:
#- Attribute
#- Behavior
#Class and Objects :
#- A class is a blueprint for the object.
#- To create an object we require a module or plan or blueprint which is nothing but class.

#BÀI 2:
class employee():
    name =""
    age =""
    salary =""
    hoursworked =""

    def __init__(self,name,age,salary,hoursworked): 
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.salary = int(input("Salary: ")) 
        self.hoursworked = int(input("Hoursworked: "))
        
    def bonus(self):
        bonus = 0 
        if self.hoursworked >=100:
            bonus = self.salary*10/100 
            with open('C:\Users\admin\Downloads\trenlop\doc.txt','w', encoding="utf-8") as f:
                f.write(self.name)
                f.write(self.age)
                f.write(self.salary)
                f.wirte(self.hoursworked)
        else:
            bonus
    
    def ouput(self):
        print("Name; ", self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        print("Hours Worked: ",self.hoursworked)
        
employee = employee("",0,0,0)