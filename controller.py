import time
import flet as ft
import model as md

# Controller : Questo componente agisce come intermediario tra il modello e la vista.
# Il controller riceve le richieste dall'utente attraverso la vista, elabora tali richieste,
# interagisce con il modello per ottenere o modificare i dati e infine aggiorna la vista in
# base ai risultati ottenuti.

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

# Rispetto al lab 03 il metodo handleSentence può essere modificata per accettare in ingresso un ulteriore
# campo “modality”, in modo da selezionare dall’esterno l’algoritmo di ricerca richiesto.
    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

# La funzione handleSpellCheck è in grado di avviare l’algoritmo di ricerca selezionato sulla
# frase inserita dall’utente. In questa funzione, prima di richiamare il metodo in grado di
# ritornare le parole sbagliate e il tempo impiegato a trovarle (funzione handleSentence() del
# lab03), è necessario inserire vari controlli su l’inserimento del linguaggio e della modalità di
# ricerca. Qualora mancasse uno o più campi, visualizzare un messaggio nell’interfaccia. Una
# volta eseguito correttamente l’algoritmo di ricerca, la funzione “handleSpellCheck” dovrà
# riportare sull’interfaccia: 1. La frase inserita, 2. Le parole errate e 3. Il tempo richiesto dalla
# ricerca. Infine, alla pressione del tasto, il metodo si dovrà occupare anche di svuotare il
# TextField che contiene la frase.
    def handleSpellCheck(self, e):
        txtCurrentSentence = self._view.txtIn.value
        if txtCurrentSentence =="":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Add a sentence!"))
            return
        language = self._view.ddLanguage.value
        print(language)
        modality = self._view.ddSelectModality.value
        print(modality)

        if language == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select a language!"))
            return

        if modality == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select a modality!"))
            return

        parole, elapsedTime = self.handleSentence(txtCurrentSentence, language, modality)

        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text("Frase inserita: "+txtCurrentSentence))
        self._view.txtOut.controls.append(ft.Text("Parole errate: " + parole))
        self._view.txtOut.controls.append(ft.Text("Tempo richiesto dalla ricerca: "+ str(elapsedTime)))
        self._view.update()
    def handleLanguageSelection(self, e):
        print("Avvenuta corretta selezione della lingua")
        self._view.txtOut.controls.append(ft.Text(value="Language correctly selected: " + self._view.ddLanguage.value))
        self._view.update()

    def handleSelectSearchMode(self, e):
        print("Avvenuta corretta selezione della modalità")
        self._view.txtOut.controls.append(ft.Text(value="Modality correctly selected: "+self._view.ddSelectModality.value))
        self._view.update()

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text