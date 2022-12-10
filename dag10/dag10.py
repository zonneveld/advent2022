#ster 1
with open("dag10.data") as data:
    data = data.read().split("\n")
    data = [i.split(" ") + ['0'] for i in data]
    cycles = [1]
    for c,v,*_ in data:
        if c == "addx":
            cycles.append(cycles[-1])
        cycles.append(cycles[-1]+int(v))
    awnser = sum([cycles[i-1] * i for i in [20,60,100,140,180,220]])
    print(awnser)

 
#ster 2
with open("dag10.data") as data:
    data = data.read().split("\n")
    data = [i.split(" ") + ['0'] for i in data]
    cycles = [1]
    for c,v,*_ in data:
        if c == "addx":
            cycles.append(cycles[-1])
        cycles.append(cycles[-1]+int(v))
    for y in range(0,240,40):
        row = ""
        for x in range(0,40):
            row +=  "#" if cycles[y+ x] in [x-1,x,x+1] else "."
        print(row)
