lopoci = [[], [2, 6, 7], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [1]]


def pronadji_najkraci_put(karta, todor_a, koraljka_b):
    if todor_a == koraljka_b:
        return 0
    putevi = [[todor_a]]
    while len(putevi) > 0:
        put = putevi.pop(0)
        cvor = put[-1]
        susjedi = karta[cvor]
        for susjed in susjedi:
            if susjed not in put:
                novi_put = put[:]
                novi_put.append(susjed)
                putevi.append(novi_put)
                if susjed == koraljka_b:
                    # print(f'Put: {" -> ".join(map(str, novi_put))}')
                    return len(novi_put) - 1


print(pronadji_najkraci_put(lopoci, int(input()), int(input())))