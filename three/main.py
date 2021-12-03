import itertools
import collections

PositionValue = collections.namedtuple("PositionValue", ['position', 'value'])

def position_counts(input_strings):

    positions = sorted([PositionValue(i,v) for line in input_strings for i,v in enumerate(line) ], key=lambda pv: pv.position)
    position_groups = itertools.groupby(positions, key=lambda pv: pv.position)

    test = {k: collections.Counter([i.value for i in g]) for k,g in position_groups }

    return  test

def most_common(counter):
    return counter.most_common(1)[0][0]

def least_common(counter):
    return counter.most_common()[-1][0]

def to_digit(binary_string):
    return int(binary_string, 2)

def rates(position_counts):
    return (
    "".join([most_common(c) for k, c in position_counts.items()]),
    "".join([least_common(c) for k, c in position_counts.items()]),
    )


