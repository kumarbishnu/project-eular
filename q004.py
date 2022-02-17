question = '''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

digits = 3


def solution():
    largest = 0
    for i in range(10 ** digits - 1, 10 ** (digits - 1), -1):
        if i % 11 == 0:
            j_max = 10 ** digits - 1
            j_inc = -1
        else:
            j_max = (10 ** digits - 1) // 11 * 11
            j_inc = -11

        for j in range(j_max, 10 ** (digits - 1), j_inc):
            x = i * j
            if x <= largest:
                break
            if str(x) == str(x)[::-1]:
                largest = x

    print(largest)

