from resources.factors import get_prime_factors

question = '''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

target = 906609


def solution():
    print(get_prime_factors(600851475143)[-1])
