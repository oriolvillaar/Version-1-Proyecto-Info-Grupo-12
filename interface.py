import tkinter as tk
from airports import *

#Creem llista on guardar els aeroports
airports = []


def UpdateList():
    #Esborrem el contingut actual
    listbox.delete(0, tk.END)
    #Iniciem el recorregut
    i = 0
    while i < len(airports):
        text = airports[i].ICAO + " | " + str(airports[i].latitude) + " | " + str(airports[i].longitude) + " | " + str(airports[i].isSchengen)
        listbox.insert(tk.END, text)
        i = i + 1


def LoadButton():
    # Indiquem que treballarem amb la variable global airports
    global airports

    # Llegim el nom del fitxer escrit per l'usuari
    filename = entry_file.get().strip()

    # Carreguem els aeroports del fitxer
    airports = LoadAirports(filename)

    # Actualitzem el valor Schengen de tots els aeroports carregats
    i = 0
    while i < len(airports):
        SetSchengen(airports[i])
        i = i + 1

    # Actualitzem la llista visual de la interfície
    UpdateList()

    # Mostrem quants aeroports s'han carregat
    label_result.config(text="Airports loaded: " + str(len(airports)))


def AddButton():
    try:
        # Llegim el codi ICAO i les coordenades introduïdes
        code = entry_code.get().strip().upper()
        lat = float(entry_lat.get())
        lng = float(entry_lng.get())

        # Creem un nou objecte Airport amb aquestes dades
        airport = Airport(code, lat, lng)

        # Calculem si és Schengen o no
        SetSchengen(airport)

        # Intentem afegir-lo a la llista
        AddAirport(airports, airport)

        # Actualitzem la llista visual
        UpdateList()

        # Mostrem missatge de confirmació
        label_result.config(text="Airport processed")
    except:
        # Si hi ha error en les dades introduïdes, mostrem missatge d'error
        label_result.config(text="Error in airport data")


def RemoveButton():
    # Llegim el codi ICAO que l'usuari vol eliminar
    code = entry_code.get().strip().upper()

    # Intentem eliminar l'aeroport de la llista
    result = RemoveAirport(airports, code)

    # Mostrem un missatge segons si s'ha trobat o no
    if result:
        label_result.config(text="Airport removed")
    else:
        label_result.config(text="Airport not found")


def SetSchengenButton():
    # Recorrem tots els aeroports per actualitzar-ne el valor Schengen
    i = 0
    while i < len(airports):
        SetSchengen(airports[i])
        i = i + 1

    # Actualitzem la llista visual
    UpdateList()

    # Mostrem missatge de confirmació
    label_result.config(text="Schengen updated")


def SaveButton():
    # Llegim el nom del fitxer on es guardaran els aeroports Schengen
    filename = entry_save.get()

    # Guardem els aeroports Schengen en el fitxer
    result = SaveSchengenAirports(airports, filename)

    # Mostrem si el procés ha anat bé o no
    if result:
        label_result.config(text="Schengen airports saved")
    else:
        label_result.config(text="Error saving file")


def PlotButton():
    # Mostrem el gràfic amb el nombre d'aeroports Schengen i no Schengen
    PlotAirports(airports)


    label_result.config(text="Plot shown")


def MapButton():
    # Generem el fitxer KML amb la informació
    MapAirports(airports)


    label_result.config(text="KML file created")


def ShowSelectedButton():
    # Obtenim la posició de l'element seleccionat
    selected = listbox.curselection()

    # Comprovem que hi hagi algun element seleccionat
    if len(selected) > 0:
        # Obtenim l'índex de l'aeroport seleccionat
        index = selected[0]
        airport = airports[index]

        # Esborrem el text anterior del panell de sortida
        text_output.delete("1.0", tk.END)

        # Mostrem les dades
        text_output.insert(tk.END, "ICAO: " + airport.ICAO + "\n")
        text_output.insert(tk.END, "Latitude: " + str(airport.latitude) + "\n")
        text_output.insert(tk.END, "Longitude: " + str(airport.longitude) + "\n")
        text_output.insert(tk.END, "Schengen: " + str(airport.isSchengen) + "\n")


# Creem la finestra principal de la interfície
root = tk.Tk()

# Definim el títol de la finestra
root.title("Airport Interface")

# Definim la mida de la finestra
root.geometry("900x600")

# Etiqueta per indicar el camp de càrrega de fitxer
label1 = tk.Label(root, text="Load file:")
label1.grid(row=0, column=0)

# Caixa de text per escriure el nom del fitxer a carregar
entry_file = tk.Entry(root, width=20)
entry_file.grid(row=0, column=1)

# Posem un nom de fitxer per defecte
entry_file.insert(0, "Airports.txt")

# Botó per carregar els aeroports del fitxer
button_load = tk.Button(root, text="Load Airports", command=LoadButton)
button_load.grid(row=0, column=2)

# Etiqueta del camp ICAO
label2 = tk.Label(root, text="ICAO:")
label2.grid(row=1, column=0)

# Caixa de text per introduir el codi ICAO
entry_code = tk.Entry(root, width=10)
entry_code.grid(row=1, column=1)

# Etiqueta del camp latitud
label3 = tk.Label(root, text="Latitude:")
label3.grid(row=2, column=0)

# Caixa de text per introduir la latitud
entry_lat = tk.Entry(root, width=10)
entry_lat.grid(row=2, column=1)

# Etiqueta del camp longitud
label4 = tk.Label(root, text="Longitude:")
label4.grid(row=3, column=0)

# Caixa de text per introduir la longitud
entry_lng = tk.Entry(root, width=10)
entry_lng.grid(row=3, column=1)

# Botó per afegir un aeroport
button_add = tk.Button(root, text="Add Airport", command=AddButton)
button_add.grid(row=4, column=0)

# Botó per eliminar un aeroport
button_remove = tk.Button(root, text="Remove Airport", command=RemoveButton)
button_remove.grid(row=4, column=1)

# Botó per actualitzar la informació Schengen dels aeroports
button_set = tk.Button(root, text="Set Schengen", command=SetSchengenButton)
button_set.grid(row=4, column=2)

# Etiqueta del camp per indicar el fitxer de guardat
label5 = tk.Label(root, text="Save file:")
label5.grid(row=5, column=0)

# Caixa de text per escriure el nom del fitxer on guardar
entry_save = tk.Entry(root, width=20)
entry_save.grid(row=5, column=1)

# Posem un nom de fitxer de sortida per defecte
entry_save.insert(0, "SchengenAirports.txt")

# Botó per guardar els aeroports Schengen
button_save = tk.Button(root, text="Save Schengen", command=SaveButton)
button_save.grid(row=5, column=2)

# Botó per mostrar el gràfic d'aeroports
button_plot = tk.Button(root, text="Plot Airports", command=PlotButton)
button_plot.grid(row=6, column=0)

# Botó per generar el fitxer KML
button_map = tk.Button(root, text="Map Airports", command=MapButton)
button_map.grid(row=6, column=1)

# Botó per mostrar la informació detallada de l'aeroport seleccionat
button_show = tk.Button(root, text="Show Selected", command=ShowSelectedButton)
button_show.grid(row=6, column=2)

# Llista on es mostren tots els aeroports carregats o afegits
listbox = tk.Listbox(root, width=70, height=20)
listbox.grid(row=7, column=0, columnspan=3)

# Zona de text on es mostren els detalls de l'aeroport seleccionat
text_output = tk.Text(root, width=40, height=10)
text_output.grid(row=7, column=3)

# Etiqueta inferior per mostrar missatges de resultat o estat
label_result = tk.Label(root, text="Ready")
label_result.grid(row=8, column=0, columnspan=3)

# Iniciem el bucle principal de la interfície gràfica
root.mainloop()