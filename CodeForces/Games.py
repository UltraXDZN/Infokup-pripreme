n = input
h, a = zip(*[n().split() for i in 'x' * int(n())])
print(sum(h.count(i) for i in a))
