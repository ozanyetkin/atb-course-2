def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

result = 1
for i in range(1, 6):
    result *= i

print(result)