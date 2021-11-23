n = int(input())
print(round(n / 2 + [0, 0.5][int(n / 2) !=  (n / 2)]) * [1, -1][n % 2 != 0])
