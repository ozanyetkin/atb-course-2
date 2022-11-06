class Person:
    # Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Getter
    def greet(self):
        return f"Merhaba! Benim adim {self.name}, yasim {self.age}"

    # Modifier
    def old(self):
        self.age += 1

    # Setter
    def change_name(self, name):
        self.name = name

person_1 = Person("ayse", 19)
person_2 = Person("ahmet", 23)

print(person_1.name)
print(person_2.name)

print(person_1.greet())
print(person_2.greet())

person_1.old()
person_2.change_name("ali")

print(person_1.greet())
print(person_2.greet())

print(person_2.age)
