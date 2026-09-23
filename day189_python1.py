class Dog:
    def sound(self):
        print("Dog says: Bark")


class Cat:
    def sound(self):
        print("Cat says: Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
