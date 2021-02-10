broj_prvi = input()
broj_drugi = input()
broj_treci = input()
broj_cetvrti = input()

unos_brojevi = [broj_prvi, broj_drugi, broj_treci, broj_cetvrti]

dvoznamenkasti = []
cetveroznamenkasti = []

dvoznamenkasti = [unos_brojevi[0] + unos_brojevi[1],
                  unos_brojevi[1] + unos_brojevi[0],
                  unos_brojevi[2] + unos_brojevi[3],
                  unos_brojevi[3] + unos_brojevi[2]]

cetveroznamenkasti = [unos_brojevi[0] + unos_brojevi[1] + unos_brojevi[2] + unos_brojevi[3],
                      unos_brojevi[0] + unos_brojevi[1] + unos_brojevi[3] + unos_brojevi[2],
                      unos_brojevi[1] + unos_brojevi[0] + unos_brojevi[2] + unos_brojevi[3],
                      unos_brojevi[1] + unos_brojevi[0] + unos_brojevi[3] + unos_brojevi[2],

                      unos_brojevi[2] + unos_brojevi[3] + unos_brojevi[0] + unos_brojevi[1],
                      unos_brojevi[2] + unos_brojevi[3] + unos_brojevi[1] + unos_brojevi[0],
                      unos_brojevi[3] + unos_brojevi[2] + unos_brojevi[0] + unos_brojevi[1],
                      unos_brojevi[3] + unos_brojevi[2] + unos_brojevi[1] + unos_brojevi[0],
                      ]


brojevi_dvoznamenkasti = list(map(int, dvoznamenkasti))
brojevi_cetveroznamenkasti = list(map(int, cetveroznamenkasti))
print(max(brojevi_dvoznamenkasti))
print(max(brojevi_cetveroznamenkasti))

