numbers = [1, 2, 3, 4]

index = 0
for number in numbers:
    print(number)
    print(index)
    index = index + 1

for i, number in enumerate(numbers):
    print(i, number)

for i in range(10):
    print(i)

for i in range(10):
    print(i)
    if i == 5:
        break
