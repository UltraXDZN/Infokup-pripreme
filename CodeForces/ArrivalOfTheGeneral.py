n = int(input())
a = [int(x) for x in input().split()]
print(a.index(max(a)) + a[::-1].index(min(a)) - (a.index(max(a)) + a[::-1].index(min(a)) >= n))
