def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 - L'arrivée dans le monde magique.")
    print("2. Quitter le jeu.")
    return input()

def lancer_choix_menu():
    dico_maison = {"Gryffondor": 0,"Serpentard": 0,"Poufsouffle": 0,"Serdaigle":0}
    menu = afficher_menu_principal()
