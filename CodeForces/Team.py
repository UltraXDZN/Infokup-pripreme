num_of_solutions_submited = 0
for i in range(int(input())):
    solution = input()
    if solution.count("1") >= 2:
        num_of_solutions_submited += 1

print(num_of_solutions_submited)
