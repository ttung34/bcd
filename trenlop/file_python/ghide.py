class Vehicle:
    def max_speed(self):
        print("Max speed is 100km/h:  ")
        
class Car(Vehicle):
    #Overridden the implementation of Vehicle class
    def max_speed(self):
        super().max_speed()# Sử dụng lại đoạn code từ lớp cha
        print("Max speed is 200km/h:  ")
    
car = Car()
car.max_speed()