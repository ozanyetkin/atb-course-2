a = 1
b = 1
fibonacci_nums = [a, b]

for _ in range(100):
    fibonacci_nums.append(fibonacci_nums[-2] + fibonacci_nums[-1])
    print(fibonacci_nums)
