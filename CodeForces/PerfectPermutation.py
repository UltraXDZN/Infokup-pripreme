n = int(input())

nums = []
for i in range(n):
    if n > 1:
        nums.append(i + 1)
        3
if n % 2 != 0:
    print(-1)
else:
    for i in range(n - 1):
        if i % 2 == 0:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(*nums)
