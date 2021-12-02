def read_file():
    values = []
    with open('input.txt','r') as f:
        for readline in f:
            vals = readline.split()
            values.append((vals[0],int(vals[1])))
    return values

def exec_commands(commands):
    horiz, depth = 0, 0
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
    return horiz * depth

def exec_aim(commands):
    horiz, depth, aim = 0, 0, 0
    for cmd in commands:
        match cmd:
            case ("forward", x):
                horiz += x
                depth += aim * x
            case ("up", x):
                aim -= x
            case ("down", x):
                aim += x
    return horiz * depth

commands = read_file()
final = exec_commands(commands)
print("1:", final)

final = exec_aim(commands);
print("2:", final)