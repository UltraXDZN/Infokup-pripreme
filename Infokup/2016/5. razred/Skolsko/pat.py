pat_koraci = []
mat_koraci = []
pat_mat_koraci = []
for i in range(4):
    pat_koraci.append(int(input()))

for i in range(4):
    mat_koraci.append(int(input()))

pat_mat_koraci.append([pat_koraci[0], mat_koraci[0]])
for i in range(1, 4):
    pat_mat_koraci.append([pat_koraci[i] + pat_koraci[i-1], mat_koraci[i] + mat_koraci[i-1]])

for i in range(4):
    print("PAT" if pat_mat_koraci[i][0] > pat_mat_koraci[i][1] else "MAT")