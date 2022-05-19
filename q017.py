question = '''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

target = 1000

units = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',

}
tens = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety'
}


def get_word(num: int):
    if num == 0:
        return ''

    if num in units.keys():
        return units[num]

    if num in range(20, 100):
        word = tens[num // 10]
        if num % 10 != 0:
            word += f'-{units[num % 10]}'
        return word

    word = ''
    if num % 100 != 0:
        word = ' and ' + get_word(num % 100)

    if num in range(100, 1000):
        word = units[num // 100] + ' Hundred' + word
        return word

    if num in range(10 ** 3, 10 ** 6):
        word = get_word(num // 10 ** 3) + ' Thousand ' + get_word(num % 10 ** 3)
    return word


def solution():
    _sum = 0
    for i in range(1, 1001):
        _sum += len(get_word(i).replace(' ', '').replace('-', ''))
    print(_sum)
