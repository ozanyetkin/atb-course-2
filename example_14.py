def prime_factors(num):
    prime_numbers = find_primes(num)

    for prime in prime_numbers:
        if num % prime != 0:
            prime_numbers.remove(prime)
    return prime_numbers

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

def lcm_range(num_1, num_2, min_range, max_range):
    num_1_primes = prime_factors(num_1)
    num_2_primes = prime_factors(num_2)
    
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

print(lcm_range(6, 10, 200, 300))
