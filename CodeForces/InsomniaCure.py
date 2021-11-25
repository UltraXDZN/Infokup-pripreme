k = int(input())
l = int(input())
m = int(input())
n = int(input())
dd = 0
for i in range(1, int(input()) + 1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        dd += 1

print(dd)