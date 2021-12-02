x, y, aim = 0, 0, 0
a, b = map(str, input().split())

while True:
    x += [0, int(b)][a == "forward"]
    y += [0, int(b) * aim][a == "forward"]
    aim += [0, int(b) * [-1, 1][a == "down"]][a == "up" or a == "down"]
    try:
        a, b = map(str, input().split())
    except ValueError:
        break

print(x * y)