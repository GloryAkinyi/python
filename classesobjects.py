class Person:
    name = "Joe"
    age = 31
    gender = "Male"

    def eat(self):
        print("Eating")


p = Person()
print(p.gender)
print(p.name)

p.eat()
