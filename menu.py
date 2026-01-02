from chapitres.chapitre_4 import lancer_chapitre_4_quidditch
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_1 import lancer_chapitre_1
from univers.personnage import initialiser_personnage
def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 - L'arrivée dans le monde magique.")
    print("2. Quitter le jeu.")
    return input()

def lancer_choix_menu():
    maisons = {"Gryffondor": 0,"Serpentard": 0,"Poufsouffle": 0,"Serdaigle":0}
    while True:
        menu = afficher_menu_principal()
        choix=input("Votre choix :")
        if choix =="1":
            joueur=lancer_chapitre_1()
            lancer_chapitre_2(joueur)
            lancer_chapitre_3(joueur,maisons)
            lancer_chapitre_4_quidditch(joueur,maisons)
            print("felicitation vous avez termine votre aventure a Poudlard")
            break
         elif choix=="2":
             print("Vous avez quitte le jeu")
             break
        else:
            print("choix invalide veuillez recommencer")
