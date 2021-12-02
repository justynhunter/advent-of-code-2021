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
        if cmd.Direction == "forward":
            horiz += cmd.Value
        elif cmd.Direction == "up":
            depth -= cmd.Value
            if (depth < 0):
                depth = 0
        elif cmd.Direction == "down":
            depth += cmd.Value
    
    return Position(horiz, depth)

def exec_aim(commands):
    horiz = 0
    depth = 0
    aim = 0

    for cmd in commands:
        if cmd.Direction == "forward":
            horiz += cmd.Value
            depth += aim * cmd.Value
        elif cmd.Direction == "up":
            aim -= cmd.Value
        elif cmd.Direction == "down":
            aim += cmd.Value

    return Position(horiz, depth)

commands = read_file()
final_pos = exec_commands(commands)

print(final_pos)
print(final_pos.Horizontal * final_pos.Depth)

aim_final = exec_aim(commands);

print(aim_final)
print(aim_final.Horizontal * aim_final.Depth)