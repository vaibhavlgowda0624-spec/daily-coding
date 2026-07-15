class Animal:
    def speak(self):
        print("Animal Sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

d = Dog()

d.speak()
d.bark()
