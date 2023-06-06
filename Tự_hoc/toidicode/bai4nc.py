

#Private
class Boo:
    __name = "Boo" #khai báo thuộc tính ở chuẩn private
    def __getName(self):#khai báo phương thức ở chuẩn private
        print(self.__name)
        
    def get(self):
        self.__getName()
        
print(Boo().__name)#"Foo" đối tượng không có thuộc tính "__name"
Boo().__getName()#Foo đối tượng không có thuộc tính 
Boo().get()   

class Bar(Boo):
    def getNaminBoo(self):
        self.__getName()
        
Bar().getNaminBoo()
        