
test = lambda t : -1 if (t <0) else 1  if abs(t -0) == 2 else t
loc = lambda p: [test(i) for i in p]
get = lambda h,t: t if loc(h) == h else loc(h)

sub = lambda a,b: [x - y for x,y in zip(a,b)]
add = lambda a,b: [x + y for x,y in zip(a,b)]

#ster 1
with open("dag9.data") as data:
    dir = {'R':[0,1],'D':[1,0],'L':[0,-1],'U':[-1,0]}
    commands = data.read().split("\n")
    commands = [i.split(" ") for i in commands]
    commands = [[i[0],int(i[1])] for i in commands]

    r = []
    h = [0,0]
    t = h
   
    for c,a in commands:
        for _ in range(a):
            h = add(h,dir[c])
            d = sub(t,h)
            d = get(d,[0,0])
            t = sub(t,d)
            r.append(tuple(t))
          
    print(len(set(r)))

# ster 2
with open("dag9.data") as data:
    dir = {'R':[0,1],'D':[1,0],'L':[0,-1],'U':[-1,0]}
    commands = data.read().split("\n")
    commands = [i.split(" ") for i in commands]
    commands = [[i[0],int(i[1])] for i in commands]

  
    chain = [[20,20] for _ in range(10)]
    r = []
   
    for c,a in commands:
        for _ in range(a):
            chain[0] = add(chain[0],dir[c])
            for i in range(1,len(chain)):
                t = chain[i]
                h = chain[i-1]

                d = sub(t,h)
                d = get(d,[0,0])
                
                chain[i] = sub(t,d)
            r.append(tuple(chain[-1]))

    print(len(set(r)))


            # print("#"*40)
            # for y in range(40):
            #     row = ""
            #     for x in range(40):
            #         if [x,y] in chain:
            #             row += str(chain.index([x,y]))
            #         else:
            #             row+= "."
            #     print(row)
            # print(chain)
