r, c = map(int, input().split())
to_change = input().split('|')
final = input().split('|')

ct = 0
for i in range(r):
    for j in range(c):
        if to_change[i][j] == "0" and final[i][j] == "1":
            ct += 100
        elif to_change[i][j] == "1" and final[i][j] == "0":
            ct += 1

print(ct)