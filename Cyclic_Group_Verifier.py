group = [1, 2, 3, 4, 5, 6, 7, 8, 9]
order = len(group)
modulo = 0
co_primes = []


def has_coprime(n):
    result = n
    min_prime = 2
    factors = []
    while min_prime <= n**0.5:
        if result % min_prime == 0:
            result /= min_prime
            factors.append(min_prime)
            return True

        min_prime += 1

    return False


def is_coprime(n):
    return


has_coprime(order)






# for i in range(order):
#     if order % i == 1:
#         co_primes.append(i)
#
