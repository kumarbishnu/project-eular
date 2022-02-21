import math


def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    root = math.floor(math.sqrt(n))
    i = 5
    while i <= root:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def next_two_primes(prime_list, candidate):
    for x in [1, 2]:
        i = 2
        prime = True
        root = math.floor(math.sqrt(candidate))
        while prime_list[i] <= root:
            if candidate % prime_list[i] == 0:
                prime = False
                break
            i += 1
        if prime:
            prime_list.append(candidate)
        candidate += 2 * x
    return prime_list, candidate


def get_n_primes(n: int):
    prime_list = [2, 3, 5, 7]
    if n <= 4:
        return prime_list[:n]

    candidate = 11
    while len(prime_list) < n:
        prime_list, candidate = next_two_primes(prime_list, candidate)

    return prime_list


def get_primes_upto(n: int):
    bound = (n + 1) // 2
    root_bound = (math.floor(math.sqrt(n)) + 1) // 2

    sieve = [2 * i + 1 for i in range(1, bound)]
    for i in range(1, root_bound):
        if sieve[i - 1]:
            for j in range(2*i*(i+1), bound, sieve[i - 1]):
                sieve[j - 1] = False

    return [2] + [i for i in sieve if i]
