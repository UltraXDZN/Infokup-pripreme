def find_duplicate_num(nums):
    tortoise = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[tortoise]]
        if tortoise == hare:
            break

    hare = nums[0]
    while hare != tortoise:
        hare = nums[tortoise]
        tortoise = nums[hare]

    return hare


print(find_duplicate_num([6, 5, 2, 2, 3, 1, 4]))
