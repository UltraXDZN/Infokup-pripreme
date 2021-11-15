k, n, w = map(int, input().split())
sum_bananas = 0
for i in range(1, w+1):
    sum_bananas += i * k

sum_bananas -= n
if sum_bananas < 0:
    sum_bananas = 0
print(sum_bananas)