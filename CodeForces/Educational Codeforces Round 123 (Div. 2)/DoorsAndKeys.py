def check_map():
    collected = []
    for kd in a:
        if kd.islower():
            collected.append(kd)
        elif kd.isupper() and kd.lower() not in collected:
            return "NO"
    return "YES"


for _ in range(int(input())):
    a = list(input())
    print(check_map())
