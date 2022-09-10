# 1'den 1000'e kadar olan tum asal sayilar
# bir listede olacak sekilde
prime_numbers = []

for test_number in range(1, int(input("Bir sayi giriniz: "))):
    is_prime = True

    if test_number == 1:
        is_prime = False

    for i in range(2, int(test_number ** (1 / 2))):
        if (test_number / i) % 1 == 0:
            is_prime = False

    if is_prime == True:
        prime_numbers.append(test_number)

print(prime_numbers)