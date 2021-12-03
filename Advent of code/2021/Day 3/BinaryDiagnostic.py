report = []
while True:
    a = input()
    if a == "":
        break
    report.append(a)

gamma_rate = "".join([(["0", "1"][i.count("0") < i.count("1")]) for i in
                      [[report[j][i] for j in range(len(report))] for i in range(len(report[0]))]])
epsilon = ((gamma_rate.replace("1", "a")).replace("0", "1")).replace("a", "0")

print(int(gamma_rate, 2) * int(epsilon, 2))
