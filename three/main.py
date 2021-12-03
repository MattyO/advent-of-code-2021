import itertools
import collections
import copy

PositionValue = collections.namedtuple("PositionValue", ['position', 'value'])

#def pivot_hash(hash_to_pivot, key_funtion);
#    pass

def position_counts(input_strings):

    positions = sorted([PositionValue(i,v) for line in input_strings for i,v in enumerate(line) ], key=lambda pv: pv.position)
    position_groups = itertools.groupby(positions, key=lambda pv: pv.position)

    test = {k: collections.Counter([i.value for i in g]) for k,g in position_groups }

    return  test

def most_common(counter):
    ordered = counter.most_common()

    if len(ordered) > 1 and ordered[0][1] == ordered[1][1]:
        return '1'

    return counter.most_common()[0][0]


def least_common(counter):
    ordered = counter.most_common()

    #import pdb; pdb.set_trace()

    if len(ordered) > 1 and ordered[0][1] == ordered[1][1]:
        return '0'

    return counter.most_common()[-1][0]


def to_digit(binary_string):
    return int(binary_string, 2)

def rates(position_counts):
    return (
    "".join([most_common(c) for k, c in position_counts.items()]),
    "".join([least_common(c) for k, c in position_counts.items()]),
    )


def rating(input_string, funt):
    input_string = copy.copy(input_string)

    pc = position_counts(input_string)
    number_to_compare = [funt(c) for k, c in pc.items()]

    for l in range(0, len(number_to_compare)):
        pc = position_counts(input_string)
        number_to_compare = [funt(c) for k, c in pc.items()]
        compare_portion = "".join(number_to_compare[0: l+1])
        input_string = list(filter(lambda s: s.startswith(compare_portion), input_string))

        if len(input_string) <= 1:
            break



    return input_string[0]



