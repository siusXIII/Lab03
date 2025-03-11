class Dictionary:

    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as file:
            righe = file.readlines()
            for riga in righe:
                self._dict.append(riga.strip("\n"))

    def printAll(self):
        for i in self._dict:
            print(i)


    @property
    def dict(self):
        return self._dict