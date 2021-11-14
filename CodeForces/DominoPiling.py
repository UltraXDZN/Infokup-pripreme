m, n = map(int, input().split())
print(((m * n) - ((m * n) % 2)) // 2)