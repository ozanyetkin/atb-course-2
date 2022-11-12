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

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def greet(self):
        return f"Adim {self.name}, {self.age} yasindayim"

    def play(self):
        return "Oyun oynamak cok eglenceli"

person_object = Person("Ali", 45)
print(person_object.greet())

child_object = Child("Osman", 8)
print(child_object.greet())
print(child_object.play())
