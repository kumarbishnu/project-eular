question = '''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

target = 20

routes = {}


def count_routes(m, n):
    if m == 0 or n == 0:
        return 1

    if (m, n) in routes.keys():
        return routes[(m, n)]

    routes[(m, n)] = count_routes(m, n - 1) + count_routes(m - 1, n)
    return routes[(m, n)]


def solution():
    print(count_routes(target, target))
