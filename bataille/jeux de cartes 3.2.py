from random import *


"""Definition"""


def creation():
    jeu_trie = []
    # creations des differentes variables :

    couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]          # liste des couleurs auxquelles peut appartenir une carte.
    valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]      # liste des valeurs que peut prendre une carte.
    traduction = {11: "Valet", 12: "Dame", 13: "Roi", 14: "As"} # dictionnaire pour la traduction.


    # Creation du jeu :

    for c in couleurs:
        for v in valeurs:
            #if v in traduction:  # si v est une valeur a traduire (si c'est une clef de 'traduction' -> 11, 12, 13, 14).
                #v = traduction[v]   # alors on remplace la clef pas sa valeur correspondante -> Valet, Dame, Roi, As.
            jeu_trie.append((v, c))      # on ajoute un tuple qui represente une carte ayant 2 parametres : valeur et couleur.

    """jeu = [(x, y) for y in couleurs for x in valeurs]"""
    return jeu_trie

def melanger(liste):
    """Fonction qui prend un jeu de cartes et le melange"""
    liste2 = []
    while len(liste) != 0:
        carte = choice(liste)
        liste2.append(carte)
        liste.remove(carte)
    return liste2


def distribuerj1(liste):
    jeu1 = jeu[0:26]
    return jeu1

def distribuerj2(liste):
    jeu2 = jeu[26:52]
    return jeu2



def tirer(jeu):
    a = jeu[0]
    jeu.remove(jeu[0])
    return a





def bataille(carte1, carte2, reste):
    print("BATAILLE !!!")


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
                bataille(carte1, carte2, reste)
        
        elif carte1[0] > carte2[0]:
            for k in range(len(reste)):
                jeu1.append(reste[k])
            jeu1.append(carte1)
            jeu1.append(carte2)
        
        else:
            for l in range(len(reste)):
                jeu2.append(reste[l])
            jeu2.append(carte1)
            jeu2.append(carte2)

    elif len(jeu1) == 0:
        print("Le joueur 2 remporte la partie !")
        input()

    else:
        print("Le joueur 1 remporte la partie !")
        input()



def partie():
    reste = []
    nombre_de_tours = 0
    nombre_de_batailles = 0
    # Tant qu'il reste des cartes :
    while len(jeu1) != 0 and len(jeu2) != 0:
        #print(jeu1)
        #print(jeu2)
        print("nb de cartes du joueur 1 :", len(jeu1))
        print("nb de cartes du joueur 2 :", len(jeu2))
    # On tire les cartes et on sort de la boucle infinie si c'est impossible (un des joueurs perdant):
        carte1 = tirer(jeu1)
        carte2 = tirer(jeu2)


        # On compare la valeur des 2 cartes :
        if carte1[0] > carte2[0]:
            jeu1.append(carte1)
            jeu1.append(carte2)
            print(carte1, "vs", carte2)
            print("le joueur 1 gagne !")
        elif carte2[0] > carte1[0]:
            jeu2.append(carte1)
            jeu2.append(carte2)
            print(carte1, "vs", carte2)
            print("le joueur 2 gagne !")
        # Si Ã©galitÃ© on appel le fonction bataille() :

        else:
            bataille(carte1, carte2, reste)
            nombre_de_batailles += 1
            reste = []
        nombre_de_tours += 1
        print(nombre_de_tours, "eme tour")
        print(len(jeu1))
    print("partie terminee en {0} tours avec {1} batailles".format(str(nombre_de_tours), str(nombre_de_batailles)))
    input()




"""Programme principale"""
jeu = creation()

#jeu = melanger(jeu)
jeu1 = [(3, 2), (5, 3), (6, 3) , (14, 2), (12, 2), (14, 1)]
jeu2 = [(3, 3), (5, 2), (6, 1) , (13, 1), (11, 3), (13, 2)]
partie()


