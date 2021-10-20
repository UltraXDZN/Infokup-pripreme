def pronadji_rijec_u_stihu(rijec, pjesma):
    """
    Vraca stih u kojem se nalazi rijec iz pjesme.
    :param rijec: broj koji predstavlja rijec u pjesmi
    :param pjesma: lista/skup koji se sastoji od stihova pjesme

    :type pjesma: list
    :type rijec: int
    :return:
    """

    zbroj_rijeci = 0
    for stih in pjesma:
        zbroj_rijeci += len(stih)
        if zbroj_rijeci >= rijec:
            return pjesma.index(stih) + 1
    return 0


def main():
    broj_stihova = int(input())  # Broj stihova koje korisnik unosi.

    pjesma = []  # Skup svih stihova.

    for i in range(broj_stihova):
        stih = [str(x) for x in input().split()]
        pjesma.append(stih)

    # Petlja kojom korisnik upisuje stihove te se dodaju u skup "pjesma"

    broj_rijeci = int(input())  # Broj rijeci kojima treba pronaci stih.

    rjesenja = []  # Definicija skupa za pronadjene stihove.

    for i in range(broj_rijeci):
        rjesenja.append(pronadji_rijec_u_stihu(int(input())))

    # Petlja koja pronalazi stihove na temelju korisnikovih unosa
    # te ih sprema u skup "pjesma".

    print(*rjesenja, sep='\n')  # Ispis rjesenja jednog ispod drugog.


if __name__ == "__main__":
    """
    Zadatak: Stih

    Opis:
    Mirkova pjesma ima n stihova. Napišite program koji odgovara na upite oblika: u kojem se stihu nalazi
    i-ta riječ pjesme?
    """
    main()
