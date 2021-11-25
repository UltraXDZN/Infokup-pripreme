n = int(input())
res = []
for i in range(n):
    a, b = map(int, input().split())
    res.append((b - a) % b)

print(*res, sep="\n")
