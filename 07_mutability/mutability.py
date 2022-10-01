x = 10
y = 10
x = y

print(id(x) == id(y))
print(id(y) == id(10))

x = x + 1

print(id(x) == id(y))
print(id(y) == id(10))
print(id(x) == id(11))

a = ["a", "b"]
b = ["a", "b"]

print(id(a) == id(b))

a = ["adsvcgfhx", "b", 3]
b = a

print(id(a) == id(b))

a.append("c")

print(b)

a = 10
b = a

print(id(a) == id(b))

a = a + 1

print(b)
