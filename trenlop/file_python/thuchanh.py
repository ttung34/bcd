class Animal:
    name= ""
    age = 0
    
    def info(self):
        print("name", self.name)
        print("age", self.age)
        
    def __init__(self, name, age):
        self.name = name
        self.age = age        
        
        
        
class Dog(Animal):
    def brak(self):
        print("Dog child class, A dog can brak")
  
        
class Cat(Animal):#Kế thừa lớp animalanimal
    def meow(self): #khai báo phương thức 
        print("Cat child class, A cat can meow")# in ra màn hình  chuỗi
    
    
    
dog = Dog("pub",3)
dog.info()
dog.brak()


meo = Cat("beo", 1)#khởi tạo một đối tượng
meo.info()   
meo.meow()#truy thức 2 phương thức
     