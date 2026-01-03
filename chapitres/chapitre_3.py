import json
import random
from univers.maison import actualiser_points_maison
from univers.maison import afficher_maison_gagnante
from univers.personnage import afficher_personnage

def apprendre_sorts(joueur, chemin_fichier="data/sort.json"):
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
        print("Tu viens d'apprendre le sort : {} ({})".format(sort["nom"], sort["type"]))
        input("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for sort in sort_selectionnes:
        print("- {} ({}) : {}".format(sort["nom"], sort["type"], sort["description"]))

    return joueur

def quiz_magie(joueur, chemin_fichier="data/quiz.magie.json"):
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
        print(str(i + 1) + ". " + q["question"])
        reponse = input("> ").strip()
        if reponse.lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.")
            score_quiz += 25
        else:
            print("Mauvaise réponse. La bonne réponse était :"+ str(q['reponse']))

    print("Score obtenu : {} points".format(score_quiz))
    print("La maison {} gagne {} points !".format(joueur["Maison"], score_quiz))
    return score_quiz

def lancer_chapitre_3(joueur, maisons):
    apprendre_sorts(joueur,"data/sort.json")
    resultat=quiz_magie(joueur, "data/quiz.magie.json")
    actualiser_points_maison(maisons, joueur["Maison"], resultat)
    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)
    print("Fin du Chapitre 3 ! Les cours continuent à Poudlard...")
    input("Appuyez sur ENTREE pour continuer...")


