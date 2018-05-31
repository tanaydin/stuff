from math import sqrt

primes = [2]


def is_prime(n):
    if n in primes:
        return True

    i = 2
    sqrt_n = round(sqrt(n))
    while i <= sqrt_n:
        if is_prime(i) and n % i == 0:
            return False
        i += 1
    primes.append(n)
    return True


a = is_prime(int(input("Enter Number To Check : ")))
if a:
    print("Prime")
else:
    print("Composite")
