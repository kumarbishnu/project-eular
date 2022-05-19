question = '''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

target = 20

routes = {}


# Recursive Solution
# def count_routes(m, n):
#     if m == 0 or n == 0:
#         return 1
#
#     if (m, n) in routes.keys():
#         return routes[(m, n)]
#
#     routes[(m, n)] = count_routes(m, n - 1) + count_routes(m - 1, n)
#     return routes[(m, n)]

# Iterative Solution
# def count_routes(m, n):
#     grid = [[0 for j in range(n + 1)] for i in range(m + 1)]
#
#     for i in range(m + 1):
#         grid[i][0] = 1
#     for j in range(n + 1):
#         grid[0][j] = 1
#
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             grid[i][j] = grid[i - 1][j] + grid[i][j-1]
#
#     return grid[m][n]

# Combinatorial Solution
def count_routes(n: int):
    result = 1

    for i in range(1, n + 1):
        result = result * (n + i) // i

    return result


def solution():
    print(count_routes(target))
