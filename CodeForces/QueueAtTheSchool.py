n, t = map(int, input().split())
queue = list(input())

if queue[-1] == "G":
    change = []
    for i in range(1, t + 1):
        if queue[i:].count("G") < queue[i:].count("B"):
            change.append(queue[i])
            queue.pop(0)
        else:
            change.append(queue[-i])
            queue.pop(-1)
    print(change)
print("".join(change) + "".join(queue))
