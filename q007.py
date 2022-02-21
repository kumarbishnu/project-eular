from resources.primes import get_n_primes

question = '''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

target = 10001


def solution():
    print(get_n_primes(target)[-1])
