import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.diz = md.MultiDictionary()


    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn)
        #print(self.diz.printDic(language))
        a = time.time()
        self.diz.searchWord(txtIn, language)
        b = time.time()
        print("Tempo contains:", b - a)
        a = time.time()
        self.diz.searchWordLinear(txtIn,language)
        b = time.time()
        print("Tempo Lineare:",b-a)
        a = time.time()
        self.diz.searchWordDichotomic(txtIn, language)
        b = time.time()
        print("Tempo Dichotomic:", b - a)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text