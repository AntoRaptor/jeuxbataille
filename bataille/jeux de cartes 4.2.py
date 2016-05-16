# Importation

from random import *
from tkinter import *

# Definition des fonctions

def creation():
    jeu = []
    """ creations des differentes variables """

    couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]           #liste des couleurs auxquelles peut appartenir une carte.
    valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]       #liste des valeurs que peut prendre une carte.
    traduction = {11: "Valet", 12: "Dame", 13: "Roi", 14: "As"}  #dictionnaire pour la traduction.

    """ Creation du jeu """

    for c in couleurs:
        for v in valeurs:
            #if v in traduction:  # si v est une valeur a traduire (si c'est une clef de 'traduction' -> 11, 12, 13, 14).
            #v = traduction[v]   # alors on remplace la clef pas sa valeur correspondante -> Valet, Dame, Roi, As.
            jeu.append((v, c))     # on ajoute un tuple qui represente une carte ayant 2 parametres : valeur et couleur.

    #jeu = [(x, y) for y in couleurs for x in valeurs]

    return jeu



def melanger(liste):

    """Fonction qui prend un jeu de cartes et le melange"""

    listeMelangee = []

    while len(liste) != 0:
        carte = choice(liste)
        listeMelangee.append(carte)
        liste.remove(carte)

    return listeMelangee



def tirer(liste):
    carte = liste[0]
    liste.remove(liste[0])
    return carte



def initialisation_partie():
    jeu = creation()
    jeu = melanger(jeu)
    #jeutest1 = [(3), (5), (6) , (14), (12), (14)]
    #jeutest2 = [(3), (5), (6) , (13), (11), (13)]
    jeu1 = jeu[0:26]
    jeu2 = jeu[26:52]
    global jeu1,jeu2
    return jeu1,jeu2



def bataille(jeu1, jeu2, carte1, carte2, reste, nombre_de_batailles):
    #print("BATAILLE !!!")
    nombre_de_batailles += 1

    #print(carte1, "vs", carte2)

    """On ajoute au reste les 2 cartes egales :"""

    reste.append(carte1)
    reste.append(carte2)
    """On tire les 2 cartes intermediaires qu'on ajoute au reste :"""

    if len(jeu1) != 0 and len(jeu2) != 0:

        carte_inter1 = tirer(jeu1)
        reste.append(carte_inter1)
        carte_inter2 = tirer(jeu2)
        reste.append(carte_inter2)


    elif len(jeu1) == 0:
        """print("Le joueur 2 remporte la partie !")
        input()"""

    else:
       """ print("Le joueur 1 remporte la partie !")
        input()"""

    """# On tire 2 nouvelles cartes :"""
    if len(jeu1) != 0 and len(jeu2) != 0:
        carte1 = tirer(jeu1)
        carte2 = tirer(jeu2)

    elif len(jeu1) == 0:
       """ print("Le joueur 2 remporte la partie !")
        input()"""

    else:
        """print("Le joueur 1 remporte la partie !")
        input()"""

    if len(jeu1) != 0 and len(jeu2) != 0:
        if carte1[0] == carte2[0]:
                bataille(jeu1, jeu2, carte1, carte2, reste, nombre_de_batailles)
        
        elif carte1[0] > carte2[0]:
            for k in range(len(reste)):
                jeu1.append(reste[k])
            jeu1.append(carte1)
            jeu1.append(carte2)
        
        else:
            for l in range(len(reste)):
                jeu2.append(reste[l])
            jeu2.append(carte2)
            jeu2.append(carte1)


    elif len(jeu1) == 0:
        """print("Le joueur 2 remporte la partie !")
        input()"""

    else:
       """ print("Le joueur 1 remporte la partie !")
        input()"""



def tirer_carte():
    global reste
    global nombre_de_tours
    if len(jeu1) != 0 and len(jeu2) != 0:
        nombre_carte_j1.configure(text = "Le joueur 1 a "+str(len(jeu1))+" cartes")
        nombre_carte_j1.grid(row = 3,column = 1)
        nombre_carte_j2.configure(text = "Le joeur 2 a "+str(len(jeu2))+" cartes")
        nombre_carte_j2.grid(row = 4,column = 1)
        carte1 = tirer(jeu1)
        carte2 = tirer(jeu2)
        vs = Label(launcher)
        gagnant = Label(launcher)

        if carte1[0] > carte2[0]:
            jeu1.append(carte1)
            jeu1.append(carte2)
            vs.configure(text = (str(carte1), "vs", str(carte2)))
            vs.grid(row = 5, column = 2)
            gagnant.configure(text = "Le joueur 1 gagne !")
            gagnant.grid(row = 6, column = 2)

        elif carte2[0] > carte1[0]:
            jeu2.append(carte2)
            jeu2.append(carte1)
            vs.configure(text = (str(carte1), "vs", str(carte2)))
            vs.grid(row = 5, column = 2)
            gagnant.configure(text = "Le joueur 2 gagne !")
            gagnant.grid(row = 6, column = 2)

        # Si egalite on appel le fonction bataille() :
        else:
            bataille(jeu1, jeu2, carte1, carte2, reste, nombre_de_batailles)
            reste = []

        nombre_de_tours += 1
        """print(nombre_de_tours, "eme tour")
        print(len(jeu1))"""
    elif len(jeu1) == 0:
        print("Le joueur 2 remporte la partie")
        gagnant = "joueur 2"
    else:
        print("Le joueur 1 remporte la partie")
        gagnant = "joueur 1"
    


def partie():
    #jeu1,jeu2 = initialisation_partie()
    reste = []
    nombre_de_tours = 0
    nombre_de_batailles = 0
    # Tant qu'il reste des cartes :
    nombre_de_tours += 1
    """print(nombre_de_tours, "eme tour")
    print(len(jeu1))"""
    if len(jeu1) == 0:
        print("Le joueur 2 remporte la partie")
        gagnant = "joueur 2"
    else:
        print("Le joueur 1 remporte la partie")
        gagnant = "joueur 1"
    """print("partie terminee en {0} tours avec {1} batailles".format(str(nombre_de_tours), str(nombre_de_batailles)))
    input()"""
    return gagnant



def jouer():
    global reste
    global nombre_de_tours
    global jeu1
    global jeu1
    reste = []
    jeu1,jeu2 = initialisation_partie()
    nombre_de_tours = 0
    bouton_IA.grid_forget()
    bouton_jouer.grid_forget()
    bouton_continuer.grid(row = 2, column = 1)
    bouton_continuer.configure(command = tirer_carte)
    #nombre_carte_j1.configure(text = "Le joueur 1 a "+str(len(jeu1))+" cartes")
    #nombre_carte_j1.grid(row = 3,column = 1)
    #nombre_carte_j2.configure(text = "Le joeur 2 a "+str(len(jeu2))+" cartes")
    #nombre_carte_j2.grid(row = 4,column = 1)
    
  #nom = partie()
  #  affgagnant.configure(text = nom)
  #  affgagnant.grid(row = 4, column = 4)"""

    

# Programme principale



launcher = Tk()
launcher.title("Jeu de la bataille")


bouton1 = Button(launcher,text = "Quitter",command = launcher.destroy)
bouton_jouer = Button(launcher,text = "Jouer",command = jouer)                 
bouton_IA = Button(launcher,text = "IA vs IA",command = jouer)
bouton_continuer = Button(launcher, text = "continuer")


zone_txt = Label(launcher, text = "Bonne chance !",bg="sky blue")
carte_j1 = Label(launcher)
carte_j2 = Label(launcher)
nombre_carte_j1 = Label(launcher)
nombre_carte_j2 = Label(launcher)
affgagnant = Label(launcher, text = partie, bg = "sky blue")


bouton1.grid(row = 3 , column = 3)
bouton_IA.grid(row = 3 , column = 2)
bouton_jouer.grid(row = 3 , column = 1)
zone_txt.grid(row = 1, column = 2)


launcher.mainloop()








