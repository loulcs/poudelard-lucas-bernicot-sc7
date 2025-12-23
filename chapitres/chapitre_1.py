from univers.personnage import afficher_personnage
from univers.personnage import initialiser_personnage
from utils.input_utils import demander_nombre
from utils.input_utils import demander_choix
from univers.personnage import modifier_argent
from univers.personnage import ajouter_objet



def introduction():
    print("Bienvenue dans le monde magique de Poudlard ! ")
    print("Vous êtes un jeune sorcier qui s'apprête à vivre sa première année à Poudlard.")
    print("Votre aventure commence maintenant !")

def creer_personnage():
   prenom = input("Entrez le prenom de votre personnage : ")
   nom = input("Entrez le nom de votre personnage : ")
   attribut={"courage":0,"intelligence":0,"loyauté":0,"ambition":0}
   joueur=initialiser_personnage(nom, prenom, attribut)
   print("Choisissez vos attributs:")
   for elem in attribut:
       message="Choisissez votre niveau de"+ elem +"(1-10):"
       nombre = demander_nombre(message, 1, 10)
       joueur["Attributs"][elem] = nombre
    afficher_personnage(joueur)
   return joueur

def recevoir_lettre():
   print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard... ")
   input()
   print(""" Cher élève,
         Nous avons le plaisir de vous informer que vous avez été admis à l'école de sorcellerie de Poudlard ! """)
   bonne_reponse="Oui, bien sûr!"
   reponse=demander_choix( "Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",[bonne_reponse,"Non, je préfère rester avec l’oncle Vernon... "])
   if reponse!=bonne_reponse:
       print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie:"
             "« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » "
             "Le monde magique ne saura jamais que vous existiez...")
       exit()

def renconter_hagrid(personnage):
   print('Hagrid : Salut Harry ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.' )
   reponse=demander_choix("Voulez-vous suivre Hagrid ?",["Oui","Non"] )
   if reponse=="Non":
       print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")

import json

def acheter_fournitures(personnage):
    with open("data/inventaire.json", "r", encoding="utf-8") as f:
        inventaire = json.load(f)

    objets_obligatoires = ["Baguette magique","Robe de sorcier","Manuel de potions"]

    print("Bienvenue sur le Chemin de Traverse !")
    print("Catalogue des objets disponibles :")
    options = []
    for cle in inventaire:
        nom = inventaire[cle][0]
        prix = inventaire[cle][1]
        options.append(nom)
        print(cle + ". " + nom + " - " + str(prix) + " galions")

    while objets_obligatoires != []:
        print("\nVous avez", personnage["Argent"], "galions.")
        print("Objets obligatoires restant à acheter :")
        for obj in objets_obligatoires:
            print("-", obj)

        choix = demander_choix(
            "Choisissez un objet à acheter (ou tapez 'stop' pour finir) :",
            options + ["stop"]
        )
        if choix == "stop":
            break
        prix = 0
        for cle in inventaire:
            if inventaire[cle][0] == choix:
                prix = inventaire[cle][1]

        if personnage["Argent"] < prix:
            print("Vous n'avez pas assez d'argent. Partie perdue.")
            exit()

        modifier_argent(personnage, -prix)
        ajouter_objet(personnage, "Inventaire", choix)
        print("Vous avez acheté :", choix, "(-" + str(prix) + " galions).")

        if choix in objets_obligatoires:
            objets_obligatoires.remove(choix)

    if objets_obligatoires != []:
        print("Vous avez oublié des objets obligatoires :", objets_obligatoires)
        print("Partie perdue.")
        exit()

    prix_animaux = {"Chouette": 20,"Chat": 15,"Rat": 10,"Crapaud": 5}
    print("\nVous avez", personnage["Argent"], "galions.")
    animal = demander_choix("Choisissez votre animal de compagnie :", list(prix_animaux.keys()))
    print("Voici les animaux disponibles :")
    animal_index = 1
    for animal in prix_animaux.items():
        print(animal_index,".",animal[0],"-",animal[1],"galions")
        animal_index+=1
    animal_index = demander_nombre("Quel Animal voulez-vous ?",1,4)-1
    animal = list(prix_animaux.keys())[animal_index]


    if personnage["Argent"] < prix_animaux[animal]:
        print("Vous n'avez pas assez d'argent. Partie perdue.")
        exit()

    modifier_argent(personnage, -prix_animaux[animal])
    ajouter_objet(personnage, "Inventaire", animal)
    print("Vous avez choisi :", animal)

    print("Tous les objets obligatoires ont été achetés avec succès !")
    afficher_personnage(personnage)

    def lancer_chapitre_1():
        introduction()
        personnage = creer_personnage()
        recevoir_lettre()
        renconter_hagrid(personnage)
        acheter_fournitures(personnage)
        print("Fin du Chapitre 1 ! Votre aventure commence à Poudlard...")
        afficher_personnage(personnage)
        return personnage




