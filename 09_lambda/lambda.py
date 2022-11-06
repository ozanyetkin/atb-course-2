from math import sin

x = lambda a : a + 10

def x(a):
    return a + 10

print(x(4))

y = lambda a, b : a * b

def y(a, b):
    return a * b

print(y(5, 6))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

mytripler = myfunc(3)

print(mytripler(11))

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0) , my_list))
print(filter(lambda x: (x % 2 == 0) , my_list))
print(new_list)

# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

sin_list = list(map(lambda x: sin(x), my_list))

print(sin_list)

def sin_filter(lst: list):
    sin_lst = []
    for a in lst:
        sin_lst.append(sin(a))
    return sin_list
