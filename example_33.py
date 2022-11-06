# Circle (cember) adinda bir class yaratacagiz, yaricap vererek instance olusturacagiz
# Yarattigimiz cember instance'larinin cevre ve alan bilgisini hesaplayip self'e store edecegiz
from math import pi, sqrt


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius

    def set_area(self, area):
        self.area = area
        self.radius = sqrt(area / pi)
        self.perimeter = self.get_perimeter()

    def set_perimeter(self, perimeter):
        self.perimeter = perimeter
        self.radius = perimeter / (2 * pi)
        self.area = self.get_area()

circle_1 = Circle(4)

print(circle_1.get_area())

print(f"r = {circle_1.radius}, A = {circle_1.area}, p = {circle_1.perimeter}")

circle_1.set_area(100)

print(f"r = {circle_1.radius}, A = {circle_1.area}, p = {circle_1.perimeter}")

circle_1.set_perimeter(50)

print(f"r = {circle_1.radius}, A = {circle_1.area}, p = {circle_1.perimeter}")
