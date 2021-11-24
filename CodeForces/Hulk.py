n = int(input())
quote = ""
for i in range(1, n + 1):
    if n + 1 > i > 1:
        quote += "that "
    quote += ["I love ", "I hate "][i % 2 != 0]

print(quote + "it")
