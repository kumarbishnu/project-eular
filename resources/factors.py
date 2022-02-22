def get_prime_factors(num: int):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2
    factor = 3
    root = num ** 0.5
    while num > 1 and factor <= root:
        if num % factor == 0:
            while num % factor == 0:
                factors.append(int(factor))
                num /= factor
            root = num ** 0.5
        factor += 2
    if num != 1:
        factors.append(int(num))
    return factors


def get_prime_factors_count(num: int):
    factors = {}

    if num % 2 == 0:
        factors[2] = 0
    while num % 2 == 0:
        factors[2] += 1
        num /= 2

    factor = 3
    root = num ** 0.5
    while num > 1 and factor <= root:
        if num % factor == 0:
            factors[factor] = 0
            while num % factor == 0:
                factors[factor] += 1
                num /= factor
            root = num ** 0.5
        factor += 2
    if num != 1:
        factors[int(num)] = 1
    return factors


def get_factors(num: int):
    factors = [1, num]
    root = int(num ** 0.5)
    for i in range(2, root + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    if root * root == num:
        factors.remove(root)
    return sorted(factors)
