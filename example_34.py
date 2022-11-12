import math


class Polygon:
    def __init__(self, sides):
        """Initialized with the lengths of the sides"""
        for s in sides:
            if s <= 0:
                raise ValueError("Side lengths must be positive")
        self._sides = sides
        self._name = "Polygon"

    def name(self):
        return self._name

    def area(self):
        """The area of an arbitrary polygon is unknown"""
        return None  # placeholder

    def perimeter(self):
        total = 0.0
        for s in self._sides:
            total += s
        return total


class Triangle(Polygon):
    def __init__(self, side_1, side_2, side_3):
        super().__init__([side_1, side_2, side_3])
        self._name = "Triangle"

    def name(self):
        return self._name

    def area(self):
        area_multiplier = 1
        heron = self.perimeter() / 2
        for side in self._sides:
            area_multiplier *= (heron - side)
        return math.sqrt(area_multiplier * heron)



class IsoscelesTriangle(Triangle):
    def __init__(self, side_1, side_2):
        super().__init__(side_1, side_1, side_2)
        self._name = "Isosceles " + self._name


class EquilateralTriangle(Triangle):
    def __init__(self, side_1):
        super().__init__(side_1, side_1, side_1)
        self._name = "Equilateral " + self._name


class Parallelogram(Polygon):
    def __init__(self, side_1, side_2):
        super().__init__([side_1, side_2])
    
    def perimeter(self):
        return super().perimeter() * 2
    

class Rectangle(Parallelogram):
    def __init__(self, side_1, side_2):
        super().__init__(side_1, side_2)
        self._name = "Rectangle"
    
    def name(self):
        return self._name

    def area(self):
        rectangle_area = 1
        for side in self._sides:
            rectangle_area *= side
        return rectangle_area

"""
class Square(Parallelogram):
    def __init__(self, side_1):
        super().__init__(side_1, side_1)
        self._name = "Square"

    def name(self):
        return self._name

    def area(self):
        square_area = 1
        for side in self._sides:
            square_area *= side
        return square_area
"""

class Square(Rectangle):
    def __init__(self, side_1):
        super().__init__(side_1, side_1)
        self._name = "Square"


shapelist = [
    # Polygon([1.0, 4.5, 3.1, 3.3]),
    Triangle(3.4, 5.3, 4.2),
    IsoscelesTriangle(4.1, 1),
    EquilateralTriangle(4.2),
    Rectangle(5, 4),
    Square(3.25),
]

for shape in shapelist:
    print(
        "{0} Area: {1:.3f}  Perimeter: {2:.3f}".format(
            shape.name(), shape.area(), shape.perimeter()
        )
    )

"""
Polygon Area:  Perimeter: 11.900
Triangle Area: 7.135  Perimeter: 12.900
IsoscelesTriangle Area: 2.035  Perimeter: 9.200
EquilateralTriangle Area: 7.638  Perimeter: 12.600
Rectangle Area: 20.000  Perimeter: 18.000
Square Area: 10.5625  Perimeter: 13.000
"""
