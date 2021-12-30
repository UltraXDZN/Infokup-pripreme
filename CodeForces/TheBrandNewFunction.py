n = int(input())
a = [int(x) for x in input().split()]

ans = set()
cur_ans = set()
for i in a:
    cur_ans = {i | j for j in cur_ans}
    cur_ans.add(i)
    ans.update(cur_ans)
    # print(cur_ans, ans, "----------", sep="\n") # DEBUG
print(len(ans))

