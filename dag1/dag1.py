#ster 1
with open("dag1.data") as r_data:
    data = max([sum([int(c) for c in l.split("\n")]) for l in r_data.read().split("\n\n")])
    print(data)

#ster 2
with open("dag1.data") as r_data:
    data = [sum([int(c) for c in l.split("\n")]) for l in r_data.read().split("\n\n")]
    data.sort(reverse=True)
    print(sum(data[0:3]))
