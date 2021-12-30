n = int(input())
a = [int(x) for x in input().split()]

ans = set()
cur_ans = set()
for i in range(n+1):
    for j in range(i, len(cur_ans)):
        cur_ans.add(a[i] | a[j])
    cur_ans.add(i)
    ans.update(cur_ans)
    # print(cur_ans, ans, "----------", sep="\n") # DEBUG

print(len(ans))
