num_of_stones = int(input())
stone_order = input()
take_out = 0

for i in range(num_of_stones-1):
    if stone_order[i] == stone_order[i+1]:
        take_out += 1

print(take_out)