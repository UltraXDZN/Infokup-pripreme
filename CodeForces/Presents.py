n = int(input())
a = input().split()
print(*[a.index(str(i+1))+1for i in range(n)])
