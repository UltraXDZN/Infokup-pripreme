n = int(input())
a = sorted([int(x) for x in input().split()])[::-1]
s = sum(a) // 2
for i in range(n+1):
    if sum(a[:i]) > s:
        print(len(a[:i]))
        break
