# ster 1
with open("dag2.data") as data:
    data = data.read().split("\n")
    c = 0
    for rows in data:
        a = (ord(rows[0]) - ord('A'))
        b = (ord(rows[2]) - ord('X'))
        c += (b + 1 + [3,0,6][((a-b)+3)%3])
    print(c)

# ster 2
with open("dag2.data") as data:
    data = data.read().split("\n")
    result = 0
    revolve = lambda x,l: (x+l)%l
    for rows in data:
        a = (ord(rows[0]) - ord('A'))
        b = (ord(rows[2]) - ord('X'))
        c = revolve(a+(b-1),3)
        w = [3,0,6][revolve(a-c,3)]
        result += c+1 + w
    print(result)
