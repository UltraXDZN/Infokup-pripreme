inputs = []
a = input()
while a != "":
    inputs.append(int(a))
    a = input()

c = 0
for i in range(len(inputs)):
    if inputs[i] > inputs[i - 1]:
        c += 1
print(c)
