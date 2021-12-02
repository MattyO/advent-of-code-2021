from collections import namedtuple
Poisition = namedtuple('Poisition', ['horizontal', 'depth'])

class BaseCommand():
    def parse_command(self, c):
        command_name, number = c.split()
        number = int(number)

        return (command_name, number)

    def call(self, sub, c):
        command_name, number = self.parse_command(c)
        return self.commands[command_name](sub, c)

    @property
    def commands(self):
        return {}

class Commands(BaseCommand):
    @property
    def commands(self):
        return {
                'up': self.up,
                'down': self.down,
                'forward': self.forward
                }

    def up(self, sub, c):
        command_name, number = self.parse_command(c)
        sub.depth -= number
        return sub

    def down(self, sub, c):
        command_name, number = self.parse_command(c)
        sub.depth += number
        return sub

    def forward(self, sub, c):
        command_name, number = self.parse_command(c)
        sub.horizontal += number
        return sub

class CommandsV2(BaseCommand):
    @property
    def commands(self):
        return {
                'up': self.up,
                'down': self.down,
                'forward': self.forward
                }

    def up(self, sub, c):
        command_name, number = self.parse_command(c)
        sub.aim -= number
        return sub

    def down(self, sub, c):
        command_name, number = self.parse_command(c)
        sub.aim += number
        return sub

    def forward(self, sub, c):
        command_name, number = self.parse_command(c)
        sub.horizontal += number
        sub.depth += sub.aim * number
        return sub


class Sub():
    def __init__(self, version='v1'):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.commands = {'v1':Commands(), 'v2':CommandsV2(),}[version]

    def command(self, command):
        self.commands.call(self, command)

    def position(self):
        return Poisition(self.horizontal, self.depth)


def compute_position(input_commands, v='v1'):
    sub = Sub(version=v)

    for c in input_commands:
        sub.command(c)

    return sub.position()

