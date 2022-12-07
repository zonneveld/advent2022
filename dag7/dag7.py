
import re

# ster 1
with open("dag7.data") as data:
    def add_dir():
        global commands,score
        result = [0]
        while commands:
            command = commands.pop()
            if re.search("^\d+",command):
                result[0] += int(re.match("^\d+",command)[0])
            elif re.search("^\$ cd [\w+]",command):
                result.append(add_dir())
                result[0] += result[-1][0] 
            elif re.search("\$ cd \.{2}",command):
                if result[0] < 100000:
                    score += result[0]
                return result
        return result
    commands = data.read().split("\n")
    commands.reverse()
    score = 0
    add_dir()
    print(score)

#ster 2
with open("dag7.data") as data:
    def add_dir():
        global commands,values
        result = [0]
        while commands:
            command = commands.pop()
            if re.search("^\d+",command):
                result[0] += int(re.match("^\d+",command)[0])
            elif re.search("^\$ cd [\w+]",command):
                result.append(add_dir())
                result[0] += result[-1][0] 
            elif re.search("\$ cd \.{2}",command):
                values.append(result[0])
                return result
        values.append(result[0])
        return result

    commands = data.read().split("\n")
    commands.reverse()
    values = []
    add_dir()
    values.sort()
    result = next(x for x in values if ((70000000 - values[-1]) + x) > 30000000)
    print(result)


