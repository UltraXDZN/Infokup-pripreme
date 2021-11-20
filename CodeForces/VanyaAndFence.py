n, h = map(int, input().split())
heights = [int(x) for x in input().split()]
width = 0
for i in range(n):
    if heights[i] <= h:
        width += 1
        continue
    width += 2

print(width)
