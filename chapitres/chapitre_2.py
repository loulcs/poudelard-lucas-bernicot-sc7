from utils.input_utils import demander_choix
from univers.maison import repartition_maison
from univers.personnage import afficher_personnage
import json

def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    choix_ron = demander_choix("Que répondez-vous ?",["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."])
    if choix_ron == "Bien sûr, assieds-toi !":
        joueur["Attributs"]["loyauté"] += 1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
    else:
        joueur["Attributs"]["ambition"] += 1
        print("Ron fronce les sourcils mais respecte votre choix.")

    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu 'Histoire de la Magie' ?")
    choix_hermione = demander_choix("Que répondez-vous ?",["Oui, j’adore apprendre de nouvelles choses !", "Euh… non, je préfère les aventures aux bouquins."])
    if choix_hermione == "Oui, j’adore apprendre de nouvelles choses !":
        joueur["Attributs"]["intelligence"] += 1
        print("Hermione sourit : — Super, tu vas adorer Poudlard !")
    else:
        joueur["Attributs"]["courage"] += 1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour !")

    print("Puis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choix_drago = demander_choix("Comment réagissez-vous ?",["Je lui serre la main poliment.", "Je l’ignore complètement.", "Je lui réponds avec arrogance."])
    if choix_drago == "Je lui serre la main poliment.":
        joueur["Attributs"]["ambition"] += 1
        print("Drago hoche la tête : — Hum… intéressant.")
    elif choix_drago == "Je l’ignore complètement.":
        joueur["Attributs"]["loyauté"] += 1
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
    else:
        joueur["Attributs"]["courage"] += 1
        print("Drago semble surpris, mais vous n’êtes pas impressionné.")
    print("Le train continue sa route. Le château de Poudlard se profile à l’horizon...")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")
    print("Tes attributs mis à jour :", joueur["Attributs"])

def mot_de_bienvenue():
    print("Le professeur Dumbledore se lève et s’adresse à toute l’assemblée :\n")
    print("""Bonsoir à tous ! Nous voici enfin réunis pour une nouvelle année à Poudlard.
Le château se réjouit d'être à nouveau rempli de visages souriants et de la gaité de la jeunesse.
Je suis Albus Dumbledore, votre Directeur. Comme il est de coutume, je vous rappelle que, comme ne manquera pas de vous le dire Mr Rusard, il est impératif de respecter le règlement intérieur de l'école.
Ainsi, je rappelle aux nouveaux comme aux anciens que la Forêt est absolument interdite aux élèves.
De même, il est interdit d'utiliser la magie en dehors des cours ainsi que d'entrer dans le couloir du troisième étage.
Enfin, il existe une liste d'objets interdits que Mr Rusard ne manquera pas de vous communiquer.""")
    input("Appuyez sur Entrée pour continuer...")


def ceremonie_repartition(joueur):
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]

    print("La cérémonie de répartition commence dans la Grande Salle...")
    print("Le Choixpeau magique t’observe longuement avant de poser ses questions.")
    maison = repartition_maison(joueur, questions)
    joueur["Maison"] = maison
    print(f"Le Choixpeau s’exclame : {maison} !!!")
    print(f"Tu rejoins les élèves de {maison} sous les acclamations !")



def installation_salle_commune(joueur):
    with open("data/maisons.json", "r", encoding="utf-8") as f:
        maisons = json.load(f)
    maison_joueur =joueur["Maison"]
    info_maison = maisons[maison_joueur]
    description = info_maison["description"]
    message_installation = info_maison["message_installation"]
    couleurs = info_maison["couleurs"]
    emoji = info_maison["emoji"]

    print("Vous suivez les préfets à travers les couloirs du château...")
    print(emoji,description)
    print(message_installation)
    print("Les couleurs de votre maison : {}".format(", ".join(couleurs)))


def lancer_chapitre_2(joueur):
    rencontrer_amis(joueur)
    mot_de_bienvenue()
    ceremonie_repartition(joueur)
    installation_salle_commune(joueur)
    input("Appuyez sur Entrée pour continuer...")
    print("Résumé de votre personnage à la fin du chapitre 2 :")
    afficher_personnage(joueur)
    print("Fin du Chapitre 2 ! Les cours à Poudlard vont bientôt commencer...")




