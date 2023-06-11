from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile

pr = ManagerFile()

g = pr.obGrafoSinText(GrafoNoDirigido)


if __name__ == "__main__":
    print(g)