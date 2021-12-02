def read_file():
    values = []
    with open('input.txt','r') as f:
        for readline in f:
            values.append(int(readline))
    return values

def count_increases(values):
    previous = values.pop(0)
    increases = 0;

    for val in values:
        if previous < val:
            increases += 1
        previous = val
    return increases

def sum_windows(values):
    windows = []
    for idx, val in enumerate(values):
        if idx+2 >= len(values):
            break
        windows.append(val + values[idx+1] + values[idx+2])
    return windows

values = read_file()
increases = count_increases(values)

print('increases', increases)

windows = sum_windows(values)
window_increases = count_increases(windows)

print('window increases', window_increases)