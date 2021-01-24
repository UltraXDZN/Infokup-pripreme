prvi_let = int(input())
kasnjenje = int(input())
prvi_let_f = int(input())
drugi_let_f = int(input())
treci_let_f = int(input())

let = (prvi_let + kasnjenje)
if let <= prvi_let_f:
    print(1)
elif let <= drugi_let_f:
    print(2)
else:
    print(3)