from resources.factors import get_factors

question = '''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

target = 20


def solution():
    primes = []
    for i in range(2, target):
        temp = primes
        factors = get_factors(i)
        for i in factors:
            if i in temp:
                temp.remove(i)
        primes.extend(factors)
        print(i, factors)
    product = 1
    for i in primes:
        product *= i
    print(product)
    # lcm = 1
    # for i in range(2, target):
    #     if i > lcm:
    #         greater = i
    #     else:
    #         greater = lcm
    #     while True:
    #         if greater % i == 0 and greater % lcm == 0:
    #             lcm = greater
    #             break
    #         greater += 1
