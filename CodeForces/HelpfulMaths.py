sum_of_nums = input().split("+")

for i in range(len(sum_of_nums)):
    is_sorted = True
    for j in range(len(sum_of_nums)-1):
        if sum_of_nums[j] > sum_of_nums[j+1]:
            sum_of_nums[j], sum_of_nums[j+1] = sum_of_nums[j+1], sum_of_nums[j]
            is_sorted = False

    if is_sorted:
        break

print(*sum_of_nums, sep="+")
