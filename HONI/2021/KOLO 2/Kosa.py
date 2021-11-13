n, m = map(int, input().split())
a, x = map(int, input().split())
b, y = map(int, input().split())

i = 1
while n <= m:
    if i % a == 0 and i % b == 0:
        n += 2 * (x + y)
    elif i % a == 0:
        n += x
    elif i % b == 0:
        n += y
    i += 1
print(i-1)