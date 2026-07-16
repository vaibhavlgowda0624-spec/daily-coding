class Bird:
    def fly(self):
        print("Bird Flying")

class Eagle(Bird):
    def fly(self):
        print("Eagle Flying High")

for obj in [Bird(), Eagle()]:
    obj.fly()
