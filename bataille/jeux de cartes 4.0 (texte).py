from random import *


"""Definition"""


def creation():
    jeu = []
    # creations des differentes variables :

    couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]          # liste des couleurs auxquelles peut appartenir une carte.
    valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]      # liste des valeurs que peut prendre une carte.
    traduction = {11: "Valet", 12: "Dame", 13: "Roi", 14: "As"} # dictionnaire pour la traduction.


    # Creation du jeu :

    for c in couleurs:
        for v in valeurs:
            #if v in traduction:  # si v est une valeur a traduire (si c'est une clef de 'traduction' -> 11, 12, 13, 14).
                #v = traduction[v]   # alors on remplace la clef pas sa valeur correspondante -> Valet, Dame, Roi, As.
            jeu.append((v, c))      # on ajoute un tuple qui represente une carte ayant 2 parametres : valeur et couleur.

    """jeu = [(x, y) for y in couleurs for x in valeurs]"""
    return jeu



def choix(liste):
    a = randrange(len(liste))
    return liste[a]



def melanger(liste):
    """Fonction qui prend un jeu de cartes et le melange"""
    listeMelangee = []
    while len(liste) != 0:
        carte = choix(liste)
        listeMelangee.append(carte)
        liste.remove(carte)
    return listeMelangee



def distribuerj1(liste):
    jeu1 = jeu[0:26]
    return jeu1



def distribuerj2(liste):
    jeu2 = jeu[26:52]
    return jeu2



def tirer(jeu):
    carte = jeu[0]
    jeu.remove(jeu[0])
    return carte



def bataille(carte1, carte2, reste, nombre_de_batailles, traduction):
    print("BATAILLE !!!")
    nombre_de_batailles += 1

    #print(carte1, "vs", carte2)
    # On ajoute au reste les 2 cartes egales :
    reste.append(carte1)
    reste.append(carte2)
    # On tire les 2 cartes intermediaires qu'on ajoute au reste :
    if len(jeu1) != 0 and len(jeu2) != 0:

        carte_inter1 = tirer(jeu1)
        reste.append(carte_inter1)
        carte_inter2 = tirer(jeu2)
        reste.append(carte_inter2)


    elif len(jeu1) == 0:
        print("Le joueur 2 remporte la partie !")
        input()

    else:
        print("Le joueur 1 remporte la partie !")
        input()

    # On tire 2 nouvelles cartes :
    if len(jeu1) != 0 and len(jeu2) != 0:
        carte1 = tirer(jeu1)
        carte2 = tirer(jeu2)

    elif len(jeu1) == 0:
        print("Le joueur 2 remporte la partie !")
        input()

    else:
        print("Le joueur 1 remporte la partie !")
        input()

    if len(jeu1) != 0 and len(jeu2) != 0:
        if carte1[0] == carte2[0]:
                bataille(carte1, carte2, reste, nombre_de_batailles, traduction)
        
        elif carte1[0] > carte2[0]:
            if carte1[0] in traduction:
                carte_traduite1 = (traduction.get(carte1[0]), carte1[1])
            else:
                carte_traduite1 = carte1
            if carte2[0] in traduction:
                carte_traduite2 = (traduction.get(carte2[0]), carte2[1])
            else:
                carte_traduite2 = carte2
            print(carte_traduite1[0], "de", carte_traduite1[1], "vs", carte_traduite2[0], "de", carte_traduite2[1])
            print("le joueur 1 gagne la bataille !")

            for k in range(len(reste)):
                jeu1.append(reste[k])
            jeu1.append(carte1)
            jeu1.append(carte2)
        
        else:
            if carte1[0] in traduction:
                carte_traduite1 = (traduction.get(carte1[0]), carte1[1])
            else:
                carte_traduite1 = carte1
            if carte2[0] in traduction:
                carte_traduite2 = (traduction.get(carte2[0]), carte2[1])
            else:
                carte_traduite2 = carte2
            print(carte_traduite1[0], "de", carte_traduite1[1], "vs", carte_traduite2[0], "de", carte_traduite2[1])
            print("le joueur 2 gagne la bataille !")

            
            for l in range(len(reste)):
                jeu2.append(reste[l])
            jeu2.append(carte2)
            jeu2.append(carte1)

    elif len(jeu1) == 0:
        print("Le joueur 2 remporte la partie !")
        input()

    else:
        print("Le joueur 1 remporte la partie !")
        input()



def partie():
    traduction = {11: "Valet", 12: "Dame", 13: "Roi", 14: "As"} # dictionnaire pour la traduction.
    reste = []
    nombre_de_tours = 0
    nombre_de_batailles = 0
    # Tant qu'il reste des cartes :
    while len(jeu1) != 0 and len(jeu2) != 0:
        print("nb de cartes du joueur 1 :", len(jeu1))
        print("nb de cartes du joueur 2 :", len(jeu2))
        # On tire 2 cartes !
        carte1 = tirer(jeu1)
        carte2 = tirer(jeu2)


        # On compare la valeur des 2 cartes :
        if carte1[0] > carte2[0]:
            jeu1.append(carte1)
            jeu1.append(carte2)
            if carte1[0] in traduction:
                carte_traduite1 = (traduction.get(carte1[0]), carte1[1])
            else:
                carte_traduite1 = carte1
            if carte2[0] in traduction:
                carte_traduite2 = (traduction.get(carte2[0]), carte2[1])
            else:
                carte_traduite2 = carte2
            print(carte_traduite1[0], "de", carte_traduite1[1], "vs", carte_traduite2[0], "de", carte_traduite2[1])
            print("le joueur 1 gagne !")
        elif carte2[0] > carte1[0]:
            jeu2.append(carte2)
            jeu2.append(carte1)
            if carte1[0] in traduction:
                carte_traduite1 = (traduction.get(carte1[0]), carte1[1])
            else:
                carte_traduite1 = carte1
            if carte2[0] in traduction:
                carte_traduite2 = (traduction.get(carte2[0]), carte2[1])
            else:
                carte_traduite2 = carte2
            print(carte_traduite1[0], "de", carte_traduite1[1], "vs", carte_traduite2[0], "de", carte_traduite2[1])
            print("le joueur 2 gagne !")
        # Si egalite on appel le fonction bataille() :
        else:
            bataille(carte1, carte2, reste, nombre_de_batailles, traduction)
            reste = []
        nombre_de_tours += 1
        print(nombre_de_tours, "eme tour")
        print(len(jeu1))
    if len(jeu1) == 0:
        print("Le joueur 2 remporte la partie")
    else:
        print("Le joueur 1 remporte la partie")
    print("partie terminee en {0} tours avec {1} batailles".format(str(nombre_de_tours), str(nombre_de_batailles)))
    input()




"""Programme principale"""
jeu = creation()

jeu = melanger(jeu)
#jeutest1 = [(3), (5), (6) , (14), (12), (14)]
#jeutest2 = [(3), (5), (6) , (13), (11), (13)]
jeu1 = distribuerj1(jeu)
jeu2 = distribuerj2(jeu)
partie()


