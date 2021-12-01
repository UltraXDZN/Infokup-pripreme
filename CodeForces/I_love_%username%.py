n = int(input())
s = [int(i) for i in input().split()]
x = s[:1]
for p in s:
    n -= min(x) <= p <= max(x)
    x += [p]

print(n)
