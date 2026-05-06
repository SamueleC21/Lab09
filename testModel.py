from model.model import Model

model = Model()
model.buildGrafo(4000)
print(model.NumNodes())
print(model.NumArchi())
print(model._grafo.edges)