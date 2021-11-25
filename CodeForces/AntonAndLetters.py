line = ((input().replace("{", '')).replace('}', '')).replace(', ', '')
num = 0
i = 0
while len(line) != 0:
    line = line.replace(line[0], '')
    num += 1
    i += 1

print(num)