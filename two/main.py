from collections import namedtuple
Poisition = namedtuple('Poisition', ['horizontal', 'depth'])

def compute_position(input_commands):
    current_position =Poisition(0,0)

    for c in input_commands:
        command_name, number = c.split()
        number = int(number)

        #import pdb; pdb.set_trace()

        if command_name == 'forward':
            current_position = Poisition(current_position.horizontal + number, current_position.depth)
        elif command_name == 'down':
            current_position = Poisition(current_position.horizontal, current_position.depth + number)
        elif command_name == 'up':
            current_position = Poisition(current_position.horizontal, current_position.depth - number)


    return current_position
