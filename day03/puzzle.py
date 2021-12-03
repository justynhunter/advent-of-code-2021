def read_file():
    values = []
    with open('input.txt','r') as f:
        lines = f.read().splitlines()
        for l in lines:
            chars = []
            for c in l:
                chars.append(int(c))
            values.append(chars)
    return values

def count(report):
    results = [[0,0], [0,0], [0,0], [0,0], [0,0],[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    for r in report:
        for i in range(12):
            results[i][r[i]] += 1
    return results

def gamma(result):
    g = []
    for i in result:
        if (i[1] > i[0]):
            g.append(1)
        else:
            g.append(0)
    return g

def epsilon(result):
    e = []
    for i in result:
        if (i[1] > i[0]):
            e.append(0)
        else:
            e.append(1)
    return e

report = read_file()
result = count(report)
g = gamma(result)
e = epsilon(result)

print(g)
print(e)
