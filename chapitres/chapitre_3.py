import json
import random

from univers.maison import actualiser_points_maison


def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    # Chargement des sorts depuis le fichier JSON
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        tous_sorts = json.load(f)
    categories = {"Offensif": [], "Défensif": [], "Utilitaire": []}
    for sort in tous_sorts:
        type_sort = sort["type"]
        if type_sort in categories:
            categories[type_sort].append(sort)
    sort_selectionnes = []
    sort_selectionnes.append(random.choice(categories["Offensif"]))
    sort_selectionnes.append(random.choice(categories["Défensif"]))
    utilitaires = []
    while len(utilitaires) < 3:
        sort = random.choice(categories["Utilitaire"])
        if sort not in utilitaires:
            utilitaires.append(sort)

    for sort in utilitaires:
        sort_selectionnes.append(sort)

    joueur["Sortilèges"] = []
    for sort in sort_selectionnes:
        joueur["Sortilèges"].append(sort["nom"])
        print(f"Tu viens d'apprendre le sort : {sort['nom']} ({sort['type']})")
        input("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for sort in sort_selectionnes:
        print(f"- {sort['nom']} ({sort['type']}) : {sort['description']}")

    return joueur


def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.")

    questions_choisies = []
    while len(questions_choisies) < 4:
        q = random.choice(questions)
        if q not in questions_choisies:
            questions_choisies.append(q)

    score_quiz = 0
    for i in range(4):
        q = questions_choisies[i]
        print(f"{i + 1}. {q['question']}")
        reponse = input("> ").strip()
        if reponse.lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.\n")
            score_quiz += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']}\n")

    print(f"Score obtenu : {score_quiz} points")

from univers.maison import actualiser_points_maison
from univers.maison import afficher_maison_gagnante
from univers.personnage import afficher_personnage

def lancer_chapitre_3(joueur, maison):
    apprendre_sorts(maison)
    quiz_magie(maison)
    actualiser_points_maison(maison)
    afficher_maison_gagnante(maison)
    afficher_personnage(joueur)

