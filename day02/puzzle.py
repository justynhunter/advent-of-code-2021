from collections import namedtuple

Command = namedtuple("Command", "Direction Value")
Position = namedtuple("Position", "Horizontal Depth")

def read_file():
    values = []
    with open('input.txt','r') as f:
        for readline in f:
            vals = readline.split()
            values.append(Command(vals[0],int(vals[1])))
    return values

def exec_commands(commands):
    horiz = 0
    depth = 0
    for cmd in commands:
        match cmd:
            case ("forward", x):
                horiz += x
            case ("up", x):
                depth -= x
                if (depth < 0):
                    depth = 0
            case ("down", x):
                depth += x    
    return Position(horiz, depth)

def exec_aim(commands):
    horiz = 0
    depth = 0
    aim = 0

    for cmd in commands:
        match cmd:
            case ("forward", x):
                horiz += x
                depth += aim * x
            case ("up", x):
                aim -= x
            case ("down", x):
                aim += x
    return Position(horiz, depth)

commands = read_file()
final_pos = exec_commands(commands)

print("1:", final_pos.Horizontal * final_pos.Depth)

aim_final = exec_aim(commands);

print("2:", aim_final.Horizontal * aim_final.Depth)