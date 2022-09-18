# Bir adet sayiyi girdi olarak alacagiz,
# Bu sayiya kadar olan ve bu sayiyla aralarinda asal olan tum sayilari verecek
# (Birbirlerine bolunemeyen) == (Ortak bolenleri sadece 1 olan)
# 12 verirsek eger cikti [1, 5, 7, 11] olmali
from example_14 import find_primes

def prime_factors(num):
    prime_numbers = find_primes(num)

    for prime in prime_numbers:
        if num % prime != 0:
            prime_numbers.remove(prime)
    return prime_numbers

def find_co_primes(input_num):
    co_primes = []
    prime_facs = prime_factors(input_num)
    print(prime_facs)
    for num in range(input_num):
        for prime in prime_facs:
            if num % prime != 0:
                co_primes.append(num)
    return co_primes

print(find_co_primes(20))