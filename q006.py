question = '''
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

target = 100


def solution():
    _sum = target * (target + 1) // 2
    _sum_of_squares = (2 * target + 1) * (target + 1) * target // 6
    print(_sum ** 2 - _sum_of_squares)
