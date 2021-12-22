n, q = input().split()
s = input()
ans = s.count("abc")
s = [i for i in s]
for i in range(int(q)):
    id_num, val = input().split()
    ans -= [0, 1]["abc" in "".join(s[max(0, int(id_num) - 3):int(id_num) + 2])]
    s[int(id_num)-1] = val
    ans += [0, 1]["abc" in "".join(s[max(0, int(id_num) - 3):int(id_num) + 2])]
    print(ans)
