num_of_tests = int(input())
sequences = []
sequences_lens = []
for i in range(num_of_tests):
    sequences_lens.append(int(input()))
    sequences.append([int(x) for x in input().split()])

disassemble = []
for i in range(num_of_tests):
    original_squence = []
    for j in range(sequences_lens[i]):
        if j % 2 == 0:
            original_squence.append(sequences[i][j])
        else:
            original_squence.append(sequences[i][-(j+1)])
        print(original_squence)
    print("-----------------")
    disassemble.append(original_squence)

for i in range(len(disassemble)):
    print(*disassemble[i])
