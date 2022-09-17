def addition(a, b):
    return a + b

def addition(lst: list):
    # bu arada fonksiyon ne gerektiriyorsa onu yapabilir
    sum = 0
    for e in lst:
        sum += e
    return sum

print(addition([3, 5, 7]))
print(addition([9, 2, 19]))
# print(addition(["a", "b", "c"]))
