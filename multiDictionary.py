import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.parole = []
        self.diz = {"italian": d.Dictionary(), "english": d.Dictionary(), "spanish": d.Dictionary()}
        self.diz["italian"].loadDictionary("./resources/Italian.txt")
        self.diz["english"].loadDictionary("./resources/English.txt")
        self.diz["spanish"].loadDictionary("./resources/Spanish.txt")

    def printDic(self, language):
        for i in self.diz.keys():
            if i == language:
                self.diz[i].printAll()

    def searchWord(self, words, language):
        parts = words.split(" ")
        for word in parts:
            if self.diz[language].dict.__contains__(word):
                word = rw.RichWord(word)
                word.corretta = True
            else:
                word = rw.RichWord(word)
                word.corretta = False
                print(word)
            self.parole.append(word)
        return self.parole

    def searchWordLinear(self, words, language):
        parts = words.split(" ")
        for word in parts:

            if word in self.diz[language].dict:
                word = rw.RichWord(word)
                word.corretta = True
            else:
                word = rw.RichWord(word)
                word.corretta = False
                print(word)
            self.parole.append(word)
        return self.parole

    def searchWordDichotomic(self, words, language):
        # Ensure the dictionary is sorted
        sorted_dict = sorted(self.diz[language].dict)

        def dichotomic_search(word_list, target):
            low = 0
            high = len(word_list) - 1

            while low <= high:
                mid = (low + high) // 2
                mid_word = word_list[mid]

                if mid_word == target:
                    return True
                elif mid_word < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        parts = words.split(" ")
        for word in parts:
            rich_word = rw.RichWord(word)

            if dichotomic_search(sorted_dict, word):
                rich_word.corretta = True
            else:
                rich_word.corretta = False
                print(rich_word)

            self.parole.append(rich_word)

        return self.parole