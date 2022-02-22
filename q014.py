question = '''
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

target = 1000000

collatz = {1: 1}


def count_chain(num: int):
    if num in collatz.keys():
        return collatz[num]

    if num % 2 == 0:
        collatz[num] = 1 + count_chain(num // 2)
    else:
        collatz[num] = 2 + count_chain((3 * num + 1) // 2)

    return collatz[num]


def solution():
    start = 0
    max_chain = 0
    for i in range(target // 2, target):
        count = count_chain(i)
        collatz[i] = count
        if count >= max_chain:
            max_chain = count
            start = i
    print(start)
