pocetni_broj = int(input())
zavrsni_broj = int(input())


class Graph():
    def __init__(self, lista_nodova=[]):
        self.lista_nodova = lista_nodova


class Node():
    edge = []

    def __init__(self, broj):
        self.broj = broj


class Edge():
    def __init__(self, node_prvi, node_drugi, udaljenost):
        self.node_prvi = node_prvi
        self.node_drugi = node_drugi
        self.udaljenost = udaljenost

    def reverse(self):
        self.node_prvi, self.node_drugi = self.node_drugi, self.node_prvi


nodovi = [ Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(10), Node(11), Node(12), Node(13), Node(14) ]
edgeovi = []

for i in range(7):
    edgeovi.append(Edge(nodovi[i], nodovi[i+1], 10))

for i in range(8, 14):
    edgeovi.append(Edge(nodovi[i], nodovi[i+1], 30))

graf = Graph()

print(brojac)
