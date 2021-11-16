n, k = map(int, input().split())

while k > 0:
    n = [n // 10, n - 1][n % 10 > 0]
    k -= 1

print(n)
