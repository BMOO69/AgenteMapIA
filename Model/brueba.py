import Model.ManagerFile
from Model.GrafoNoDirigido import GrafoNoDirigido

mana = Model.ManagerFile.ManagerFile()
grafo = mana.obGrafoSinText(GrafoNoDirigido)

print(grafo)

pos=(12,12)
if __name__ == "__main__":
    print(pos[0] + pos[1])
    print(str(pos)+"adasda")