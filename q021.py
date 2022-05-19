from resources.factors import get_factors

question = '''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, 
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

target = 10000


def solution():
    amicable = []
    for i in range(2, target):
        if i in amicable:
            continue
        a = sum(get_factors(i)[:-1])
        if a == i:
            continue
        b = sum(get_factors(a)[:-1])
        if i == b:
            amicable.append(i)
    print(sum(amicable))
