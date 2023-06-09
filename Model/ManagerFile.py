from io import open


class ManagerFile(object):

    __instance = None
    def __new__(cls, *args, **kwargs):
        if ManagerFile.__instance is None:
            ManagerFile.__instance = object.__new__(cls)
        return ManagerFile.__instance

    def obtenerGrafo(self):
        fileedge = open("aristaGra.txt","r")
        listAr = fileedge.readlines()
        fileedge.close()
        return listAr

#if __name__ == "__main__":
 #   uso1 = ManagerFile()
  #  tr = uso1.obtenerGrafo()

   # for i in tr:
    #    print(i)


