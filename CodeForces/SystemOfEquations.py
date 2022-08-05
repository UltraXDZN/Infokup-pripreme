n, m = map(int, input().split())

c = 0
s = n + m
for a in range(s):
    for b in range(s):
        if (a * a + b) == n and (a + b * b) == m:
            c += 1

print(c)
