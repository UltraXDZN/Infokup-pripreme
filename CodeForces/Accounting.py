a, b, n = map(int, input().split())
check = False
for i in range(-1000, 1001):
    if a * i ** n == b:
        print(i)
        check = True
        break

if not check:
    print("No solution")
# print(x)