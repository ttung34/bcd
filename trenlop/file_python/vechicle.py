#basse class
class Vehicle:
    def vehicle_info(self):
        print("Vehicle class")

#Child class
class Car(Vehicle):
    def car_info(self):
        print("Car class")
        
        
class SportsCar(Vehicle):
    def Sports_car_info(self):
        print("Sportscar class")
        
my_car = SportsCar()

my_car.Sports_car_info()#truy suất vào lớp con
my_car.car_info()#truy suất vào lớp cha 
my_car.vehicle_info()#Truy suất vào lớp ông

