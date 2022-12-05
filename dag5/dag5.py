#ster 1
import re
with open("dag5.data") as data:
    [grid,commands] = data.read().split("\n\n")
    grid = grid.split("\n")
    grid = list(zip(*grid[::-1]))
    field =[]
    for row in grid:
        if row[0] != ' ':
            _s = [i for i in row[1:] if i != ' ']
            field.append(_s)
    commands = commands.split("\n")
    for command in commands:
        [q,s,e] = [int(i) for i in re.findall("\d+",command)]
        for _ in range(q):
            field[e-1].append(field[s-1].pop())

    result = ''.join([r[-1] for r in field])
    print(result)

#ster 2
with open("dag5.data") as data:
    [grid,commands] = data.read().split("\n\n")
    grid = grid.split("\n")
    grid = list(zip(*grid[::-1]))
    field =[]
    for row in grid:
        if row[0] != ' ':
            _s = [i for i in row[1:] if i != ' ']
            field.append(_s)
    commands = commands.split("\n")
    for command in commands:
        [q,s,e] = [int(i) for i in re.findall("\d+",command)]
        t = []
        for _ in range(q):
            t = [field[s-1].pop()] + t
        field[e-1]+= t

    result = ''.join([r[-1] for r in field])
    print(result)
