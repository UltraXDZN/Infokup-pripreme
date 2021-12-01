inputs = []
a = input()
while a != "":
    inputs.append(int(a))
    a = input()

c = 0
new_inputs = []

for i in range(len(inputs) - 2):
    b = (inputs[i] + inputs[i + 1] + inputs[i + 2])
    new_inputs.append(b)

for i in range(len(new_inputs)):
    if new_inputs[i] > new_inputs[i - 1]:
        c += 1

print(c)
