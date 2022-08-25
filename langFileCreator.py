from tkinter import *

nombrelangue = 3
fichier = "lang.language"
langue = ['VarName', 'English', 'French']

screen = Tk()
text = ""

screen.title("langEditor")


firstChamp = Entry(screen, exportselection=False)
USEntry = Entry(screen, exportselection=False)
FREntry = Entry(screen, exportselection=False)

h1 = None
h2 = None
h3 = None

c1r1 = None
c1r2 = None
c1r3 = None
c2r1 = None
c2r2 = None
c2r3 = None

c3r1 = None
c3r2 = None
c3r3 = None

lIndice1 = None
lIndice2 = None
lIndice3 = None


def affichageLangFIle():
    global h1
    global h2
    global h3
    global c1r1
    global c1r2
    global c1r3
    global c2r1
    global c2r2
    global c2r3

    global c3r1
    global c3r2
    global c3r3

    global lIndice1
    global lIndice2
    global lIndice3

    """affichage Fichier Lang"""

    file = open(fichier, 'r')
    treederniere = file.readlines()[-3:]
    dico = {"VarName": [], "USName": [], "FRName": []}
    for i in treederniere:
        txt = ""
        indice = 0
        while i[indice] != '0':
            txt += i[indice]
            indice += 1
        dico["VarName"].append(txt)
        txt = ""
        indice += 1
        while i[indice] != '1':
            txt += i[indice]
            indice += 1
        dico["USName"].append(txt)
        txt = ""
        indice += 1
        while i[indice] != '/':
            txt += i[indice]
            indice += 1
        dico["FRName"].append(txt)
    file.close()
    file = open(fichier, 'r')
    taille = len(file.readlines())
    file.close()

    Label(screen, pady=20).grid(column=1, row=0)
    Label(screen).grid(column=1, row=6)
    Label(screen).grid(column=1, row=7)
    Label(screen, padx=20).grid(column=0, row=7)
    Label(screen, pady=5).grid(column=0, row=12)
    Label(screen, padx=5).grid(column=5, row=7)

    h1 = Label(screen, text='VarName', bg='red').grid(column=1, row=8)
    h2 = Label(screen, text='US', bg='red').grid(column=2, row=8)
    h3 = Label(screen, text='FR', bg='red').grid(column=3, row=8)

    c1r1 = Label(screen, text=dico["VarName"][0]).grid(column=1, row=9)
    c1r2 = Label(screen, text=dico["VarName"][1]).grid(column=1, row=10)
    c1r3 = Label(screen, text=dico["VarName"][2]).grid(column=1, row=11)

    c2r1 = Label(screen, text=dico["USName"][0]).grid(column=2, row=9)
    c2r2 = Label(screen, text=dico["USName"][1]).grid(column=2, row=10)
    c2r3 = Label(screen, text=dico["USName"][2]).grid(column=2, row=11)

    c3r1 = Label(screen, text=dico['FRName'][0]).grid(column=3, row=9)
    c3r2 = Label(screen, text=dico['FRName'][1]).grid(column=3, row=10)
    c3r3 = Label(screen, text=dico['FRName'][2]).grid(column=3, row=11)

    lIndice1 = Label(screen, text=taille-2, padx=20).grid(column=4, row=9)
    lIndice2 = Label(screen, text=taille-1, padx=20).grid(column=4, row=10)
    lIndice3 = Label(screen, text=taille, padx=20).grid(column=4, row=11)

    # Styliser le tableau + voir si on peut mieux faire en stockant chaque Label dans un tableau pour pouvoir tous les modifier juste avec une boucle surtout pour destroyArray()


def destroyArray():
    global h1
    global h2
    global h3
    global c1r1
    global c1r2
    global c1r3
    global c2r1
    global c2r2
    global c2r3

    global c3r1
    global c3r2
    global c3r3

    global lIndice1
    global lIndice2
    global lIndice3

    h1.destroy()
    h2.destroy()
    h3.destroy()

    c1r1.destroy()
    c1r2.destroy()
    c1r3.destroy()

    c2r1.destroy()
    c2r2.destroy()
    c2r3.destroy()

    c3r1.destroy()
    c3r2.destroy()
    c3r3.destroy()

    lIndice1.destroy()
    lIndice2.destroy()
    lIndice3.destroy()


def getAllEntry():
    global firstChamp
    global USEntry
    global FREntry
    global text
    text += firstChamp.get() + "0" + USEntry.get() + "1" + FREntry.get() +"/"
    file = open(fichier, 'a')
    file.write(text+"\n")
    file.close()
    firstChamp.delete(0, len(firstChamp.get()))
    USEntry.delete(0, len(USEntry.get()))
    FREntry.delete(0, len(FREntry.get()))
    text = ""
    affichageLangFIle()


boutonValidate = Button(screen, text="Validate", command=getAllEntry)

for i in range(nombrelangue):
    Label(screen, text=langue[i]).grid(column=1, row=i+1)

firstChamp.grid(column=2, row=1)
USEntry.grid(column=2, row=2)  # a faire en stockant des bouton dans un tablo et donc en genere * nb langue
FREntry.grid(column=2, row=3)  # a faire en stockant des bouton dans un tablo et donc en genere * nb langue
boutonValidate.grid(column=2, row=4)

affichageLangFIle()

mainloop()
