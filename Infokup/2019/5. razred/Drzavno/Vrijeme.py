n = input()
time = []

for i in range(len(n) + 1):
    s = n[:i]
    m = n[i:]

    if s == '':
        hours = 0
    elif int(s) < 24:
        hours = int(s)
    else:
        continue

    if m == '':
        minutes = 0
    elif int(m) < 60:
        if str(int(m)) != m:
            continue
        minutes = int(m)
    else:
        continue

    time.append(f'{hours}:{minutes}')

if len(time) > 0:
    time = list(set(time))
    for t in time:
        print(t)
else:
    print('TLE')