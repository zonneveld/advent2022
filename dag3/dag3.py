#ster 1
with open("dag3.data") as data:
    lookup_table = list(range(26+0,26+26)) + [0 for _ in range(6)] + list(range(0,26))
    lookup = lambda x: lookup_table[ord(x) - ord('A')]
    c= 0    
    for row in data.read().split("\n"):
        check_list = [0 for _ in range(0,len(lookup_table))]
        for item in [lookup(i) for i in row[0:len(row)//2]]:
            check_list[item] = 1
        for item in [lookup(i) for i in row[len(row)//2:]]:
            c += check_list[item] * (item + 1) 
            check_list[item] = 0
    print(c)

#ster 2
with open("dag3.data") as data:
    lookup_table = list(range(26+0,26+26)) + [0 for _ in range(6)] + list(range(0,26))
    lookup = lambda x: lookup_table[ord(x) - ord('A')]
    tri_check = lambda *x: int(sum(x) is len(x))
    c= 0
    s = 3    
    data = data.read().split("\n")
    for r in range(len(data)//s):
        check_lists = [[0 for _ in range(0,len(lookup_table))] for _ in range(s)]
        for i in range(len(check_lists)):
            for item in [lookup(x) for x in data[r*s + i]]:
                check_lists[i][item] = 1
        result = list(map(tri_check,*check_lists))
        for i in range(len(result)):
            c+= result[i] * (i+1)
    print(c)
