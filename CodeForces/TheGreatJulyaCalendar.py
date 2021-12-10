n = int(input())

i = 0
while n > 0:
    if n != 0:
        i += 1
    nums = [int(i) for i in list(str(n))]
    n -= max(nums)

print(i)
