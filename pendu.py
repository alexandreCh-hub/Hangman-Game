#ajouter des mots dans la liste
#mettre en exe
#changer les couleurs

from random import choice
from tkinter import *

def restart():
    entry.delete(0,END)
    label_title.config(text="Nombre de joueurs ?")
    image = PhotoImage(file="images/pendu0.png")
    canvas.itemconfig(container, image=image)
    canvas.image = image
    mot_secret.config(text="")
    msg.config(text="")
    lettres_donnees.config(text="")
    essai.set(10)
    global l_mot, l_donnees
    l_mot = []
    l_donnees=[]
    button.config(command=click)

def stop():
    pass

def defaite():
    mot_str = mot.get()
    label_title.config(text="C'est perdu, le mot était:")
    mot_secret.config(text=mot_str)
    msg.config(text="")
    button.config(command=stop)

def pendu(nb):
    if nb==9:
        image = PhotoImage(file="images/pendu1.png")
    elif nb==8:
        image = PhotoImage(file="images/pendu2.png")
    elif nb==7:
        image = PhotoImage(file="images/pendu3.png") 
    elif nb==6:
        image = PhotoImage(file="images/pendu4.png") 
    elif nb==5:
        image = PhotoImage(file="images/pendu5.png") 
    elif nb==4:
        image = PhotoImage(file="images/pendu6.png") 
    elif nb==3:
        image = PhotoImage(file="images/pendu7.png") 
    elif nb==2:
        image = PhotoImage(file="images/pendu8.png") 
    elif nb==1:
        image = PhotoImage(file="images/pendu9.png") 
    elif nb==0:
        image = PhotoImage(file="images/pendu10.png") 
        defaite()
    canvas.itemconfig(container, image=image)
    canvas.image = image

def motValide(m): #fonction qui prend un mot en paramètre et qui renvoie si tous les caractères sont valides ou non (alphabet minuscule ou majuscule)
    valide=True
    for l in m:
        if (l<'a' or l>'z') and (l<'A' or l>'Z'):
            valide=False
    if valide==False:
        print("caractère invalide\n")
    return valide

def accent(m):
    mot=list(m)
    for l in range(len(mot)):
        if mot[l]=='é' or mot[l]=='è' or mot[l]=='ê':
            mot[l]='e'
        elif mot[l]=='â' or mot[l]=='à':
            mot[l]='a'
        elif mot[l]=='î':
            mot[l]='i'
        elif mot[l]=='ô':
            mot[l]='o'
        elif mot[l]=='û' or mot[l]=='ù':
            mot[l]='u'
    m="".join(mot)
    return m

def partie():
    mot_str = mot.get()
    mot_entier="".join(l_mot)
    
    global l_donnees
    nb_essai= essai.get()

    if nb_essai>0:
        trouve=False
        label_title.config(text="Donnez une lettre:")
        lettre = entry.get()
        entry.delete(0,END)
        lettre=lettre.lower()

        if motValide(lettre)==True:
            if len(lettre)<1:
                msg.config(text="Au moins un caractère !")
            elif len(lettre)>1:
                mot_entier=lettre
                if mot_entier!=mot_str:
                    msg.config(text="Mauvais mot...")
                    pendu(nb_essai-1)
                    essai.set(nb_essai-1)
            elif lettre in l_donnees: #si lettre a déjà été donnée
                msg.config(text="Vous avez déjà donné cette lettre !")

            else:
                l_donnees.append(lettre)
                texte = "Lettres données:\n"+",".join(l_donnees)
                lettres_donnees.config(text=texte)
                for j in range (len(mot_str)): #si la lettre est dans le mot
                    if lettre==mot_str[j]:
                        trouve=True
                        l_mot[j]=lettre #placer la lettre à sa place
                if trouve==True:
                    msg.config(text="Bien joué !")
                    #mot_secret.config(text=l_mot)
                    mot_secret.config(text=l_mot)
                    mot_entier="".join(l_mot)
                else:
                    msg.config(text="Dommage !") #si la lettre n'est pas dans le mot
                    pendu(nb_essai-1) 
                    essai.set(nb_essai-1)
        else:
            msg.config(text="Caractère invalide !")
        if mot_entier==mot_str: #si le mot est trouvé
            label_title.config(text="Bravo, le mot était:")
            mot_secret.config(text=mot_str)
            msg.config(text="")
            button.config(command=stop)
    return 0

def solo():
    with open("pendu.txt", "r") as file:
        txt=file.read()
        liste=txt.split(", ")
        choix_mot=choice(liste)
        choix_mot=accent(choix_mot)
        file.close()
    creer_liste(choix_mot)
    mot_secret.config(text=l_mot)
    if motValide(choix_mot)==False:
        print(choix_mot,": invalide")
    return choix_mot


def duel():
    mot_str = entry.get()
    entry.delete(0,END)
    if motValide(mot_str)==False or len(mot_str)<2:
        label_title.config(text="Mot invalide, réessayer!")
        button.config(command=duel)
    else:
        mot_str = mot_str.lower()
        mot_str = accent(mot_str)
        mot.set(mot_str)
        creer_liste(mot_str)
        mot_secret.config(text=l_mot)
        label_title.config(text="Donnez une lettre:")
        button.config(command=partie)

def creer_liste(mot_str):
    global l_mot
    for i in range(len(mot_str)): #remplir le mot de "_"
        l_mot.append("_")

def click():
    chiffre = entry.get()
    entry.delete(0,END)

    if chiffre=='1':
        mot.set(solo())
        label_title.config(text="Donnez une lettre:")
        button.config(command=partie)
    elif chiffre=='2':
        label_title.config(text="Choisissez un mot:")
        button.config(command=duel)
    else:
        label_title.config(text="1 ou 2 joueurs ?")

# Définition de la fenêtre de départ
window = Tk()
window.title("Jeu du pendu")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background='#d2b4de')

frame = Frame(window, bg='#d2b4de')
right_frame = Frame(frame, bg='#d2b4de')
left_frame = Frame(frame, bg='#d2b4de')

mot = StringVar()
essai = IntVar()
essai.set(10)
l_mot = []
l_donnees=[] #liste des lettres déjà données

label_title = Label(right_frame, text="Nombre de joueurs ?", font=("Arial",40), bg='#d2b4de', fg='black')
label_title.pack()

image = PhotoImage(file="images/pendu0.png")
canvas = Canvas(left_frame, width=400, height=400, bg="#d2b4de", bd=0, highlightthickness=0)
canvas.pack()
container = canvas.create_image(200, 200, image=image)

entry = Entry(right_frame, text="", font=("Arial",40), bg='#d2b4de', fg='black')
entry.pack()

button = Button(right_frame, text="Valider", font=("Arial",40), bg='#d2b4de', fg='black', command=click)
button.pack(fill=X)

mot_secret = Label(right_frame, text="", font=("Arial",40), bg='#d2b4de', fg='black')
mot_secret.pack()

msg = Label(right_frame, text="", font=("Arial",30), bg='#d2b4de', fg='black')
msg.pack()

lettres_donnees = Label(left_frame, text="", font=("Arial",30), bg='#d2b4de', fg='black')
lettres_donnees.pack()

right_frame.grid(row=0, column=1, sticky=W)
left_frame.grid(row=0, column=0, sticky=W)
frame.pack(expand=YES)

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Rejouer", command=restart)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Menu", menu=file_menu)
window.config(menu=menu_bar)

window.mainloop()