import math

from resources.primes import get_primes_upto

question = '''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

target = 20


def solution():
    primes = get_primes_upto(target)

    lcm = 1
    sqrt = target ** 0.5
    less_than_sqrt = True
    for prime in primes:
        power = 1
        if less_than_sqrt:
            if prime <= sqrt:
                power = math.floor(math.log(target) / math.log(prime))
            else:
                less_than_sqrt = False
        lcm *= prime ** power
    print(lcm)
