from collections import namedtuple
Poisition = namedtuple('Poisition', ['horizontal', 'depth'])


class Sub():
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def command(self, command):
        command_name, number = command.split()
        number = int(number)

        if command_name == 'forward':
            self.horizontal += number
        elif command_name == 'down':
            self.depth +=  number
        elif command_name == 'up':
            self.depth -= number

        #elif command_name == 'down':
        #    self.aim += number
        #elif command_name == 'up':
        #    self.aim -= number

    def position(self):
        return Poisition(self.horizontal, self.depth)


class Sub2():
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def command(self, command):
        command_name, number = command.split()
        number = int(number)

        if command_name == 'forward':
            self.horizontal += number
            self.depth += self.aim * number
        elif command_name == 'down':
            self.aim += number
        elif command_name == 'up':
            self.aim -= number

    def position(self):
        return Poisition(self.horizontal, self.depth)


def compute_position2(input_commands):
    sub = Sub2()

    for c in input_commands:
        sub.command(c)

    return sub.position()

def compute_position(input_commands):
    sub = Sub()

    for c in input_commands:
        sub.command(c)

    return sub.position()

