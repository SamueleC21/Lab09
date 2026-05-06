import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._mappa = {}

    def buildGrafo(self, x):
        nodi = DAO.getAeroporti()
        self._grafo.add_nodes_from(nodi)
        for n in nodi:
            self._mappa[n.ID] = n
        self.aggiungiArchi(x)

    def aggiungiArchi(self, x):
        conn = DAO.getEdge()
        for c in conn:
            peso = c.sommaKm/c.numVoli
            if peso >= x:
                a1 = self._mappa[c.ORIGIN_AIRPORT_ID]
                a2 = self._mappa[c.DESTINATION_AIRPORT_ID]
                self._grafo.add_edge(a1, a2, weight = peso)



    def NumNodes(self):
        return len(self._grafo.nodes)

    def NumArchi(self):
        return len(self._grafo.edges)