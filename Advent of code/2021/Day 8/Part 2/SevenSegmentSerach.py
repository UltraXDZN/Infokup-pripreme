def compare(num1, num2):
    num1, num2 = str(num1), str(num2)
    num_of_same = []
    for i in range(len(num1)):
        if num1[i] in num2 and num1[i] not in num_of_same:
            num_of_same.append(num1[i])
    return num_of_same

zbroj = 0
# default_sdn = {
#     0: "abcefg",
#     1: "cf",
#     2: "acdeg",
#     3: "acdfg",
#     4: "bcdf",
#     5: "abdfg",
#     6: "abdefg",
#     7: "acf",
#     8: "abcdefg",
#     9: "abcdfg",
# }

default_sdn = {
    2: "cf",
    4: "bcdf",
    3: "acf",
    7: "abcdefg"
}
while True:
    try:
        sdn = default_sdn.copy()
        ssd, nums = input().split("|")
        ssd = ssd.split()
        nums = nums.split()
        for num in ssd:
            for k in sdn.keys():
                if len(num) == k:
                    sdn[k] = num
                    break

        cur_nums = []
        for k in sdn.keys():
            for j in range(4):
                if len(nums[j]) == 6:
                    if len(compare(sdn[4], nums[j])) == 4:
                        cur_nums.append("9")
                        break
                    elif len(compare(sdn[7], nums[j])) == 3:
                        cur_nums.append("0")
                        break
                    else:
                        cur_nums.append("5")
                        break

                elif len(nums[j]) == 5:
                    if len(compare(sdn[7], nums[j])) == 3:
                        cur_nums.append("3")
                        break
                    elif len(compare(sdn[4], nums[j])) == 3:
                        cur_nums.append("5")
                        break
                    else:
                        cur_nums.append("2")
                        break

        print("".join(cur_nums))
    except ValueError:
        break

print(zbroj)
