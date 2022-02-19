s = input()
a = [0]
for i in range(len(s) - 1):
    a += [a[i] + (s[i] == s[i + 1])]

for i in range(int(input())):
    l, r = map(int, input().split())
    print(a[r - 1] - a[l - 1])
