import dictionary as d
import richWord as rw

# Model (Modello): Questo componente rappresenta i dati e la logica di business dell'applicazione.
# Il modello gestisce lo stato dell'applicazione e implementa le operazioni per modificarlo.
# È indipendente dalla vista e dal controller.

class MultiDictionary:

    def __init__(self):
        self._english = d.Dictionary([], "english")
        self._italian = d.Dictionary([], "italian")
        self._spanish = d.Dictionary([], "spanish")

        self._english.loadDictionary("resources/English.txt")
        self._italian.loadDictionary("resources/Italian.txt")
        self._spanish.loadDictionary("resources/Spanish.txt")

    def searchWord(self, words, language):
        # words is a list of strings
        parole = []

        for word in words:
            word = word.lower()
            found = False
            richW = rw.RichWord(word)
            if language == "english":
                if self._english.dict.__contains__(word):
                    found = True
            elif language == "italian":
                if self._italian.dict.__contains__(word):
                    found = True
            elif language == "spanish":
                if self._spanish.dict.__contains__(word):
                    found = True
            if (found):
                richW.corretta = True

            parole.append(richW)

        return parole

    def searchWordLinear(self, words, language):
        # words is a list of strings
        parole = []

        for word in words:
            word = word.lower()
            found = False
            richW = rw.RichWord(word)
            if language == "english":
                for entry in self._english.dict:
                    if entry == word:
                        found = True
            elif language == "italian":
                for entry in self._italian.dict:
                    if entry == word:
                        found = True
            elif language == "spanish":
                for entry in self._spanish.dict:
                    if entry == word:
                        found = True
            if (found):
                richW.corretta = True

            parole.append(richW)

        return parole

    def searchWordDichotomic(self, words, language):
        # words is a list of strings
        parole = []

        for word in words:
            word = word.lower()
            found = False
            richW = rw.RichWord(word)
            if language == "english":
                currentDic = self._english.dict
                found = dichotomicSearch(word, currentDic)
            elif language == "italian":
                currentDic = self._italian.dict
                found = dichotomicSearch(word, currentDic)
            elif language == "spanish":
                currentDic = self._spanish.dict
                found = dichotomicSearch(word, currentDic)
            if (found):
                richW.corretta = True

            parole.append(richW)

        return parole


def dichotomicSearch(word, currentDic):
    start = 0
    end = len(currentDic)

    while (start != end):
        mean = start + int((end - start)/2)
        currentW = currentDic[mean]
        if word == currentW:
            return True
        elif word > currentW:  # in python < applied to strings gives True if the first string is before in lexicographic order
            start = mean+1
        else:
            end = mean

    return False
