iterations = [3 ** i for i in range(19)]

for _ in range(int(input())):
    n = int(input())
    if n > 19:
        print("NO")
    else:
        print("YES")
        print(*[iterations[i] for i in range(n)])
