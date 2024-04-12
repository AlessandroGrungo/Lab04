import flet as ft

import controller as c
import view as v

# # # LAB 04 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Dopo aver fatto il fork del progetto relativo al quarto laboratorio, realizzare in linguaggio Python       #
# un’applicazione dotata di interfaccia grafica che permetta la gestione del programma atto alla correzione  #
# delle parole sviluppato nello scorso laboratorio (Lab3).                                                   #
# L’applicazione permette di selezionare la lingua (Italiano/Inglese/Spagnolo), selezionare la modalità di   #
# ricerca (Contains/Linear/Dicotomica) e di inserire la frase da sottoporre all’algoritmo di correzione.     #
# L’applicazione dovrà poi restituire la frase inserita dall’utente, l’elenco delle parole errate e il       #
# tempo richiesto dalla ricerca.                                                                             #
# # USARE PATTERN MVC  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main(page: ft.Page):
    # Setup model, view, control according to MVC pattern
    view = v.View(page)
    controller = c.SpellChecker(view)
    view.setController(controller)
    view.add_content()

ft.app(target=main)