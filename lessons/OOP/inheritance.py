# Inheritance, passing your attributes and methods


class Animal:
    
    def __init__(self, type, sound, color):
        self.type = type
        self.sound = sound
        self.color = color
        
    def soundOfAnimal(self):
        print(f"Hey I am a {self.type}, and I sounded like this {self.sound}")
    
    def colorOfAnimal(self):
        print(f"You can notice that I have a color or pattern of {self.color}")
    
    


class Dog(Animal):
    pass

class Monkey(Animal):
    pass


hepe = Dog("Dog", "Arf Arf", "Different Types")
hepeMonkey = Monkey("Monkey", "oo ah ah", "Different Types")


hepe.soundOfAnimal()
hepeMonkey.soundOfAnimal()

hepe.colorOfAnimal()
hepeMonkey.colorOfAnimal()