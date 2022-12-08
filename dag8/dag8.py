#ster 1
with open("dag8.data") as data:
    data = data.read().splitlines()
    l = range(len(data))

    test = lambda x,y : [0,x] if x > y else [1,y]
    grid =[[int(i) for i in row] for row in data]
    awnser = [[1 for _ in l] for _ in l]
    for _ in range(4):
        for y in l:
            mark = -1
            awnser[y] = list(awnser[y])
            for x in l:
                [a,mark] = test(grid[y][x],mark)
                awnser[y][x] &= a
        grid =  list(zip(*grid[::-1]))
        awnser =  list(zip(*awnser[::-1]))
    result = 0
    for [x,y] in [[x,y] for x in l for y in l]:
        result += 0 if awnser[x][y] else 1
    print(result)

#ster 2
with open("dag8.data") as data:
    data = data.read().splitlines()
    l = range(len(data))
    def find(v,l):
        for i in range(len(l)):
            if(v <= l[i]):
                return i+1
        else:
            return len(l)

    grid =[[int(i) for i in row] for row in data]
    awnser = [[1 for _ in l] for _ in l]
    for _ in range(4):
        for y in l:
            awnser[y] = list(awnser[y])
            for x in l:
                awnser[y][x] *= find(grid[y][x],grid[y][x+1:])

        grid =  list(zip(*grid[::-1]))
        awnser =  list(zip(*awnser[::-1]))
    print(max([a for b in awnser for a in b]))
