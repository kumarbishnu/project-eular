import time


def time_elapsed(function):
    start = time.time()
    function()
    end = time.time()
    print(f'Time Elapsed: {end - start}')
