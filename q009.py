import math


question = '''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
'''

target = 1000


def solution():
    s2 = target // 2
    m_limit = math.ceil(math.sqrt(s2))

    for m in range(2, m_limit):
        if s2 % m == 0:
            sm = s2 // m
            while sm % 2 == 0:
                sm = sm // 2
            if m % 2 == 0:
                k = m + 1
            else:
                k = m + 2

            while k < 2 * m and k <= sm:
                if sm % k == 0 and math.gcd(k, m) == 1:
                    d = s2 // (k * m)
                    n = k - m
                    a = d * (m*m - n*n)
                    b = 2 * d * m * n
                    c = d * (m*m + n*n)

                    print(a * b * c)
                    return
                k += 2

    # for a in range(3, (target - 3) // 3 + 1):
    #     for b in range(a + 1, (target - 1 - a) // 2 + 1):
    #         c = target - a - b
    #         if a ** 2 + b ** 2 == c ** 2:
    #             print(a * b * c)
    #             break
