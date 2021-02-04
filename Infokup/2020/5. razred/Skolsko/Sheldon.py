zamisljeni_broj = input()

counter = 0
for i in range(len(zamisljeni_broj)):
    if int(zamisljeni_broj[i]) == (i+1):
        counter += 1

print(counter)