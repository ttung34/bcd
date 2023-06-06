class SeaAnimal :
    def __init__(self, name):
        self.name = name
        
    def swim(self):
        print("Swimning")
        
class LandAnimal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking")
        
class Penguin(SeaAnimal, LandAnimal):
    def __init__(self, name):
        super() .__init__(name)
        
    def info(self):
        print("name", self.name)
        
penguin = Penguin("canhcut")
penguin.swin()
penguin.walk()

                