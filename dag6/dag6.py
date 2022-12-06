#ster 1
with open("dag6.data") as data:
    input = data.read()
    result = next(i for i in range(4,len(input)) if len(set(input[i - 4:i])) == 4 )
    print(result)

# ster 2
with open("dag6.data") as data:
    input = data.read()
    result = next(i for i in range(14,len(input)) if len(set(input[i - 14:i])) == 14 )
    print(result)
