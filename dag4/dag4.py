import re

#ster 1
with open("dag4.data") as f:
    rows = f.read().splitlines()
    c = 0
    for row in rows:
        a1,a2,b1,b2 = [int(i) for i in re.split(r"-|,",row)]
        c += int((a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2))
print(c)

#ster 2
with open("dag4.data") as f:
    rows = f.read().splitlines()
    c = 0
    for row in rows:
        a1,a2,b1,b2 = [int(i) for i in re.split(r"-|,",row)]
        [a,b] = set(range(a1,a2+1)),set(range(b1,b2+1))
        c += len(a)+len(b) > len(a.union(b))
print(c)

