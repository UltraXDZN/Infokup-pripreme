n = [int(x) for x in input().split()]
sums = []
num = 0
for item in n:
    if n.count(item) > 1 and item not in sums:
        sums.append(item)
        num += n.count(item) - 1

print(num)