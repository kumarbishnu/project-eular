from resources.primes import get_primes_upto


question = '''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

target = 2000000


def solution():
    primes = get_primes_upto(target)
    print(sum(primes))
