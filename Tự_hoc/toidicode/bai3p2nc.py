class first:
    def getClass(self):
        print("Class First")
        
class Second:
    def getClass(self):
        print("Class Second")
class Thrid(first, Second):
    def getClass(self):
        super().getClass()

third = Thrid()
third.getClass()