zbroj = 0
n, k = map(int, input().split())
num_of_kikiriki = 0
for i in range(n):
    x, y = [str(x) for x in input().split()]
    if num_of_kikiriki >= k:
        break
    elif y == "K":
        num_of_kikiriki += 1
    zbroj += int(x)


print(zbroj)