import json
import random
from univers import maison
from utils.input_utils import demander_nombre, demander_choix
from univers.maison import actualiser_points_maison, afficher_maison_gagnante
from univers.personnage import afficher_personnage

def creer_equipe(maison,equipe_data,est_joueur=False,joueur=None):
    equipe = {"nom": maison,'score': 0,'a_marque': 0,'a_stoppe': 0, 'attrape_vifdor': False,'joueurs': []}
    nouveau_joueurs=[]
    equipe_joueur = equipe_data['joueurs']
    if est_joueur==True and joueur is not None:
        nouveau_joueurs.append("{} {} (Attrapeur) ".format(joueur['Prenom'],joueur['Nom']))
        for elem in equipe_joueur[1:]:
            nouveau_joueurs.append(elem)
    else:
        for elem in equipe_joueur:
            nouveau_joueurs.append(elem)
    equipe['joueurs'] = nouveau_joueurs
    return equipe

def tentative_marque(equipe_attaque,equipe_defense,joueur_est_joueur=False):
    proba_but=random.randint(1,10)
    if proba_but>=6:
        equipe_attaque['score']+=10
        equipe_attaque['a_marque']+=1
        if joueur_est_joueur==True:
           buteur= equipe_attaque['joueurs'][0]

        else:
            buteur=random.choice(equipe_attaque['joueurs'])
        print(buteur, "de l'équipe", equipe_attaque['nom'], "tire...")
        print(buteur,"marque un but pour ",equipe_attaque['nom'],'!(+10points)')
    else:
        equipe_defense['a_stoppe']+=1
        buteur = random.choice(equipe_attaque['joueurs'])
        print(buteur, "de l'équipe",equipe_attaque['nom'],"tire...")
        print(equipe_defense['nom'],"bloque l'attaque !")

def apparition_vifdor():
    vifdor=False
    nombre=random.randint(1,6)
    if nombre==6:
        vifdor=True
    return vifdor

def attraper_vifdor(e1, e2):
    equipe_gagnante = random.choice([e1, e2])
    equipe_gagnante['attrape_vifdor'] = True
    equipe_gagnante['score'] += 150
    return equipe_gagnante

def afficher_score(e1, e2):
    print("Score actuel :")
    print("→ {} : {} points".format(e1['nom'], e1['score']))
    print("→ {} : {} points".format(e2['nom'], e2['score']))

def afficher_equipe(maison, equipe):
    print("Équipe de", maison, ":")
    for joueur in equipe['joueurs']:
        print("-", joueur)

def match_quidditch(joueur,maisons):
    with open("data/equipes_quidditch.json", "r", encoding="utf-8") as f:
        equipe = json.load(f)

    maison_aleatoire=['Gryffondor','Serpentard','Serdaigle','Poufsouffle']
    maison_joueurs=joueur["Maison"]
    for i in range(len(maison_aleatoire)):
        if maison_aleatoire[i]== maison_joueurs:
            del maison_aleatoire[i]
            break
    maison_adverse = random.choice(maison_aleatoire)
    equipe_joueur = creer_equipe(maison_joueurs, equipe[maison_joueurs], True, joueur)
    equipe_adverse = creer_equipe(maison_adverse, equipe[maison_adverse])
    print("Équipe du joueur :")
    afficher_equipe(maison_joueurs,equipe_joueur)
    print("Équipe adverse :")
    afficher_equipe(maison_adverse,equipe_adverse)
    print("""Tu joues pour {} en tant qu' Attrapeur""".format(maison_joueurs))

    print("Le rôle de l'attrapeur est de récupérer le Vif d'Or, ce qui mettra fin immédiatement au match et fera gagner 150 points à sa maison !")
    Tour = 1
    vifdor_attrape = False
    while Tour <= 20 and not vifdor_attrape:
        print("Tour {}".format(Tour))
        afficher_score(equipe_joueur, equipe_adverse)

        tentative_marque(equipe_joueur, equipe_adverse, True)
        tentative_marque(equipe_adverse, equipe_joueur, False)

        if apparition_vifdor():
            print("Le Vif d'Or est apparu !")
            gagnant_vifdor = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("Le Vif d'Or a été attrapé par {} ! (+150 points)".format(gagnant_vifdor['nom']))
            break
        input("Appuyez sur Entrée pour continuer...")
        Tour += 1
        print()

    afficher_score(equipe_joueur, equipe_adverse)

    if vifdor_attrape:
        maison_gagnante = gagnant_vifdor["nom"]
        points = gagnant_vifdor["score"]
    else:
        if equipe_joueur["score"] > equipe_adverse["score"]:
            maison_gagnante = equipe_joueur["nom"]
            points = equipe_joueur["score"]
        elif equipe_adverse["score"] > equipe_joueur["score"]:
            maison_gagnante = equipe_adverse["nom"]
            points = equipe_adverse["score"]
        else:
            print("Match nul !")
            maison_gagnante = None
            points = equipe_joueur["score"]

    if maison_gagnante:
        points_totaux = points + 500
        actualiser_points_maison(maisons, maison_gagnante, points_totaux)
        print("La maison gagnante est {} avec {} points !".format(maison_gagnante, points_totaux))

def lancer_chapitre_4_quidditch(joueur,maisons):
        print("Epreuve Quidditch")
        match_quidditch(joueur,maisons)
        print("Fin du Chapitre 4 très belle performance sur le terrain")
        afficher_maison_gagnante(maisons)
        afficher_personnage(joueur)




































