from functools import reduce
from itertools import tee, islice
import collections
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def increase_or_decrease(x,y):
    if x < y:
        return 'increase'
    elif x > y:
        return 'decrease'
    return 'no change'

def count_items(input_array, item):
    return len([i for i in input_array if i == item])

def find_changes(measurement_input):
    return [increase_or_decrease(x,y) for x,y in pairwise(measurement_input)]

def windowed_increase(measurement_input):
    return [ reduce(lambda x,y: x+y, [a,b,c]) for a,b,c in sliding_window(measurement_input, 3) ]
