question = '''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

target = 'files/p022_names.txt'


def alphabetical_value(name: str):
    value = 0
    for letter in name.upper():
        value += ord(letter) - 64
    return value


def solution():

    with open(target, 'r') as reader:
        names = [x[1:-1] for x in reader.read().split(',')]
    names.sort()

    _sum = 0
    for i in range(len(names)):
        _sum += (i + 1) * alphabetical_value(names[i])
    print(_sum)
