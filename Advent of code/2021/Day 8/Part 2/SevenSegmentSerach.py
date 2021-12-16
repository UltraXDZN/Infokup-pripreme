total = 0
while True:
    try:
        cur_sum = 0
        ssd, nums = input().split("|")
        nums = [''.join(sorted(x)) for x in nums.split()]
        digits = {''.join(sorted(part)) for part in {*ssd.split(), *nums}}
        lenght_6 = {x for x in digits if len(x) == 6}
        lenght_5 = {x for x in digits if len(x) == 5}

        num_to_s = {1: tuple((x for x in digits if len(x) == 2))[0], 7: tuple((x for x in digits if len(x) == 3))[0],
                    4: tuple((x for x in digits if len(x) == 4))[0], 8: tuple((x for x in digits if len(x) == 7))[0],
                    }
        len6 = {6: tuple((x for x in lenght_6 if len(set(x) & set(num_to_s[1])) == 1))[0],
                9: tuple((x for x in lenght_6 if len(set(x) & set(num_to_s[4])) == 4))[0],
                }

        len5 = {5: tuple((x for x in lenght_5 if len(set(x) & set(len6[6])) == 5))[0],
                3: tuple((x for x in lenght_5 if len(set(x) & set(num_to_s[1])) == 2))[0],
                }

        num_to_s.update(len5)
        num_to_s.update(len6)

        num_to_s[0], = lenght_6 - {num_to_s[6], num_to_s[9]}
        num_to_s[2], = lenght_5 - {num_to_s[5], num_to_s[3]}

        s_to_num = {v: k for k, v in num_to_s.items()}

        cur_sum += sum(10 ** (3 - i) * s_to_num[nums[i]] for i in range(4))

        total += cur_sum

    except ValueError:
        break

print(total)
