class Person:
    def __init__(self) -> None:
        pass

class Child(Person):
    def __init__(self) -> None:
        super().__init__()

class Adult(Person):
    def __init__(self) -> None:
        super().__init__()
