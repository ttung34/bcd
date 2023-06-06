class Circle:
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
        
    def Area(self):
        return 3.14*self.r**2
    def perimeter(self):
        return 2*3.14*self.r
    def A(self,x,y):
        return (x-self.a)**2+(y-self.b)**2-(self.r)**2    
    def test_Belongs(self, x,y):
        if (self.A(x,y)==0):
            print("A thuoc duong tron C ")
        else:
            print("A khong thuoc duong tron C ")

T = Circle(1,2,1)
print("dien tich hinh tron la: ",T.Area())

T.test_Belongs(1,1)
    
        
            
    
    
    
    
    
    