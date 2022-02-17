question = '''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

target = 1000


def sum_of_multiples(num: int):
    n = (target - 1) // num
    return num * n * (n + 1) / 2


def solution():
    print(sum_of_multiples(3) + sum_of_multiples(5) - sum_of_multiples(15))
