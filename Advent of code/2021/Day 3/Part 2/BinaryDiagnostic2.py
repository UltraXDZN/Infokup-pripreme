def find_final_num(report_nums, type_h_s):
    pos = 0
    while len(report_nums) > 1:
        ones = []
        zeros = []
        for i in range(len(report_nums)):
            if report_nums[i][pos] == "1":
                ones.append(report_nums[i])
            else:
                zeros.append(report_nums[i])

        if type_h_s:
            report_nums = [zeros, ones][len(ones) >= len(zeros)]
        else:
            report_nums = [zeros, ones][len(ones) < len(zeros)]
        pos += 1
    return "".join(*report_nums)

report = []
while True:
    a = input()
    if a == "":
        break
    report.append(a)

report_new = find_final_num(report[:], True)
report_new2 = find_final_num(report[:], False)

print(int(report_new, 2) * int(report_new2, 2))
