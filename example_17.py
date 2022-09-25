# Bir adet sayiyi girdi olarak alacagiz,
# Bu sayiya kadar olan ve bu sayiyla aralarinda asal olan tum sayilari verecek
# (Birbirlerine bolunemeyen) == (Ortak bolenleri sadece 1 olan)
# 12 verirsek eger cikti [1, 5, 7, 11] olmali
from example_14 import find_primes
from collections import Counter

def prime_factors(num):
    prime_numbers = find_primes(num)

    divisible_primes = []
    for prime in prime_numbers:
        if num % prime == 0:
            divisible_primes.append(prime)
    return divisible_primes

def find_co_primes(input_num):
    co_primes = []
    prime_facs = prime_factors(input_num)

    for num in range(input_num):
        for prime in prime_facs:
            if num % prime != 0:
                co_primes.append(num)
    
    co_primes_result = []
    repetition_count = len(prime_facs)

    for key, value in Counter(co_primes).items():
        if value == repetition_count:
            co_primes_result.append(key)
    return co_primes_result

print(find_co_primes(3))
