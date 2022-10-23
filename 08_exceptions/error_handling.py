a = [1, 2, 3, 4]

for i in range(5):
    try:
        print(a[i])
    except IndexError:
        print("bunu alamadim")

print("kod buraya geldi")

nums = [7, 53, 2, 8.3, 0, -5]
for num in nums:
    try:
        print(100 / num)
    except ZeroDivisionError:
        print("bir sayiyi sifira bolemezsin")

print("kod buraya da geldi")
