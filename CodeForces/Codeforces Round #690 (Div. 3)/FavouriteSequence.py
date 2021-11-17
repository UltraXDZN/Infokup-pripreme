num_of_tests = int(input())
sequences = []
sequences_lens = []
for i in range(num_of_tests):
    sequences_lens.append(int(input()))
    sequences.append([int(x) for x in input().split()])

disassemble = []

for i in range(num_of_tests):
    original_squence = []
    j = 0

    while len(sequences[i]) > 0:
        if j % 2 == 0:
            original_squence.append(sequences[i][0])
            sequences[i].pop(0)
        else:
            original_squence.append(sequences[i][-1])
            sequences[i].pop(-1)
        j += 1
    disassemble.append(original_squence)

for i in range(len(disassemble)):
    print(*disassemble[i])
