n, k = map(int, input().split())

z = 0
tfz = 0
for i in range(1, n+1):
    if 8 + (k / 60) + tfz + ((i * 5) / 60) <= 12:
        z += 1
        tfz += ((i * 5) / 60)
        continue
    break

print(z)