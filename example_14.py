def find_primes(num):
    prime_numbers = []
    for test_number in range(1, num + 1):
        is_prime = True

        if test_number == 1:
            is_prime = False

        for i in range(2, int(test_number ** (1 / 2)) + 1):
            if (test_number / i) % 1 == 0:
                is_prime = False

        if is_prime == True:
            prime_numbers.append(test_number)
    return prime_numbers

# print(find_primes(7))

def okek(num_1, num_2, min_range, max_range):
    num_1_primes = find_primes(num_1)
    num_2_primes = find_primes(num_2)

    for prime_1 in num_1_primes:
        if num_1 % prime_1 != 0:
            num_1_primes.remove(prime_1)
    
    for prime_2 in num_2_primes:
        if num_2 % prime_2 != 0:
            num_2_primes.remove(prime_2)
    
    common_primes = set(num_1_primes + num_2_primes)
    common_multiply = 1
    for prime in common_primes:
        common_multiply *= prime
    
    remainder = min_range % common_multiply
    range_start = min_range - remainder + common_multiply
    range_stop = max_range + common_multiply

    common_numbers = []
    for common_number in range(range_start, range_stop, common_multiply):
        common_numbers.append(common_number)

    return common_numbers

print(okek(6, 10, 200, 300))
