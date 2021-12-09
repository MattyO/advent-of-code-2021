import math
def parse_line(line):
    line_parts = line.split('->')
    x1, y1 =line_parts[0].split(',')
    x2, y2 =line_parts[1].split(',')

    return list(int(c) for c in [x1, y1, x2, y2])

def is_horizontal_or_vertical(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

def points(x1,y1, x2, y2):
    line_points = []
    x_step= 0
    y_step= 0
    if x1 != x2:
        x_step = int((x2 - x1) / abs(x2-x1))
    if y1 != y2:
        y_step = int((y2 - y1) / abs(y2-y1))

    line_points.append((x1, y1))
    while line_points[-1] != (x2, y2):
        last_x, last_y = line_points[-1]
        new_point = (last_x + x_step, last_y  + y_step)
        #import pdb; pdb.set_trace()
        line_points.append(new_point)

    return line_points

