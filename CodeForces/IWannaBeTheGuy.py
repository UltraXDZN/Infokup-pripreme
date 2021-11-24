n = int(input())
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
for i in range(n+1):
    if i+1 in x[1::] or i+1 in y[1::]:
        continue
    break

print("I become the guy." if i == n else "Oh, my keyboard!")

