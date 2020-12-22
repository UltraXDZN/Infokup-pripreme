mj = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dan, mjesec = [int(i) for i in input().split()]

temp_br = dan

if (dan == 31 and mjesec == 12):
    print("Dan nove godine")
    exit(0)
    
for m in range(mjesec - 1):
    dan += mj[m]
    
if dan % 28 == 0:
    print(28, dan // 28)
    
else:
    print(dan % 28, dan // 28 + 1)
