
import flet as ft

# View (Vista) : Questo componente rappresenta l'interfaccia utente dell'applicazione.
# La vista visualizza i dati contenuti nel modello e interagisce con l'utente.

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        # ROW 1: inserire un menu a tendina (hint: pacchetto flet, control Dropdown) per selezionare
        # la lingua con tre opzioni (italiano/inglese/spagnolo). Una volta selezionata l’opzione
        # desiderata la funzione richiamerà un’altra funzione per verificare la corretta selezione della
        # lingua (far comparire un messaggio nell’interfaccia se è avvenuta o meno la corretta
        # selezione)
        self.ddLanguage = ft.Dropdown(value="Choose Language", # etichetta nella casella
                                      options=[ft.dropdown.Option("italian"),
                                               ft.dropdown.Option("spanish"),
                                               ft.dropdown.Option("english")],
                                      on_change=self.__controller.handleLanguageSelection,
                                      label="Select language")

        # Row 2 parte sinistra: creare un menu a tendina (hint: pacchetto flet, control Dropdown) per
        # selezionare il tipo di ricerca con tre opzioni (Default/Lineare/Dicotomica). Una volta
        # selezionata l’opzione desiderata richiamerà un’altra funzione per verificare la corretta
        # selezione (far comparire un messaggio nell’interfaccia se è avvenuta o meno)
        self.ddSelectModality = ft.Dropdown(value="Choose Modality",  # etichetta nella casella
                                      options=[ft.dropdown.Option("Default"),
                                               ft.dropdown.Option("Linear"),
                                               ft.dropdown.Option("Dichotomic")],
                                      on_change=self.__controller.handleSelectSearchMode, width=200,
                                      label="Search Modality")
        # Row 2 parte centrale: creare uno spazio dove inserire il testo (hint: pacchetto flet, control
        # TextField)
        self.txtIn = ft.TextField(label="Add your sentence here", width=420)
        # Row 2 parte destra: creare un bottone per avviare la funzione di correzione ortografica (hint:
        # pacchetto flet, control ElevatedButton). Questo bottone, una volta cliccato, richiamerà una
        # funzione (“handleSpellCheck”) in grado di avviare l’algoritmo di ricerca selezionato sulla
        # frase inserita dall’utente.
        self.btnSpellCheck = ft.ElevatedButton(text="Spell Check", on_click=self.__controller.handleSpellCheck)
        # creo la riga 2
        row2 = ft.Row(controls=[self.ddSelectModality, self.txtIn, self.btnSpellCheck],
                      alignment=ft.MainAxisAlignment.CENTER)
        # Row 3: creare un’area di testo (hint: pacchetto flet, control ListView) in cui stampare gli
        # output del metodo “handleSpellCheck” associato al tasto. ATTENZIONE alla sintassi di
        # ListView. Per aggiungere del contenuto all’area di testo, è necessario fornire come ingresso
        # un controller e non una stringa.
        self.txtOut = ft.ListView(expand=1, spacing=10)

        self.page.add(self.ddLanguage, row2, self.txtOut)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

