def get_factors(num: int):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2
    factor = 3
    max_factor = num ** 0.5
    while num > 1 and factor <= max_factor:
        if num % factor == 0:
            while num % factor == 0:
                factors.append(int(factor))
                num /= factor
            max_factor = num ** 0.5
        factor += 2
    if num != 1:
        factors.append(int(num))
    return factors
