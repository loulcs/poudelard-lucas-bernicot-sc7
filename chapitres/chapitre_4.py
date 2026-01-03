import json
import random
from univers import maison
from utils.input_utils import demander_nombre
from utils.input_utils import demander_choix
from univers.maison import actualiser_points_maison, afficher_maison_gagnante
from univers.personnage import afficher_personnage


def creer_equipe(maison,equipe_data,est_joueur=False,joueur=None):
    equipe = {"nom": maison,'score': 0,'a_marque': 0,'a_stoppe': 0, 'attrape_vifdor': False,'joueurs': []}
    nouveau_joueurs=[]
    equipe_joueur = equipe_data[maison]['joueurs']
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
        print(buteur,"marque un but pour ",equipe_attaque['nom'],'!(+10points)')
    else:
        equipe_defense['a_stoppe']+=1
        print(equipe_defense['nom'],"bloque l'attaque !")


def apparition_vifdor():
    vifdor=False
    nombre=random.randint(1,6)
    if nombre==6:
        vifdor=True
    return vifdor


def attraper_vifdor(e1, e2):
    noms_equipes = [e1['nom'], e2['nom']]
    equipe_gagnante = random.choice(noms_equipes)
    equipe_gagnante['attrape_vifdor'] = True
    equipe_gagnante['score'] += 150
    return equipe_gagnante


def afficher_score(e1,e2):
    print("Score actuel:")
    point_actuel=e1['score']
    point_actuels=e2['score']
    print(e1['nom'],":",point_actuel,"points",'\n',e2['nom'],":",point_actuels,"points")

def afficher_equipe(maison, equipe):
    print("Équipe de", maison, ":")
    for joueur in equipe['joueurs']:
        print("-", joueur)


def match_quidditch(joueur,maisons):
    with (open ("data/equipes_quidditch.json",'r')as f):
        equipe=json.load(f)
    maison_aleatoire=['Gryffondor','Serpentard','Serdaigle','Poufsouffle']
    maison_joueurs=joueur["Maison"]
    for i in range(len(maison_aleatoire)):
        if maison_aleatoire[i]== maison_joueurs:
            del maison_aleatoire[i]
            break
    maison_adverse = random.choice(maison_aleatoire)
    equipe_joueur = creer_equipe(maison_joueurs, equipe, est_joueur=True, joueur=joueur)
    equipe_adverse = creer_equipe(maison_adverse, equipe)
    print("Équipe du joueur :")
    afficher_equipe(maison_joueurs,equipe_joueur)
    print("Équipe adverse :")
    afficher_equipe(maison_adverse,equipe_adverse)
    print("Le rôle de l'attrapeur est de récupérer le Vif d'Or, ce qui mettra fin immédiatement au match et fera gagner 150 points à sa maison !")

    Tour=1
    gagnant_vifdor = None
    while Tour<20 :
        print("Tour",Tour)
        afficher_score(equipe_joueur,equipe_adverse)
        tentative_marque(equipe_joueur,equipe_adverse,True)
        tentative_marque(equipe_adverse, equipe_joueur)

        if apparition_vifdor()==True:
            print("Le Vif d'Or est apparu !")
            gagnant_vifdor = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("Le match est terminé, le Vif d'Or a été attrapé par", gagnant_vifdor['nom'])
            break
        input("Appuyez sur ENTREE pour continuer...")
        Tour+=1
    print("Score Final :")
    afficher_score(equipe_joueur,equipe_adverse)
    if gagnant_vifdor is not None:
        maison_gagnante = gagnant_vifdor['nom']
        points = 150
    else:
        if equipe_joueur['score'] > equipe_adverse['score']:
            maison_gagnante = maison_joueur
            points = equipe_joueur['score'] + 500
        elif equipe_adverse['score'] > equipe_joueur['score']:
            maison_gagnante = maison_adverse
            points = equipe_adverse['score'] + 500
        else:
            print("Match nul ! Aucun bonus de 500 points attribué.")
            maison_gagnante = None
            points = 0
    if maison_gagnante:
        actualiser_points_maison(maisons, maison_gagnante, points)
        print(f"La maison gagnante est {maison_gagnante} avec {points} points !")
    else:
        print("Aucune maison ne remporte le match.")

def lancer_chapitre_4_quidditch(joueur,maisons):
        print("Epreuve Quidditch")
        match_quidditch(joueur,maisons)
        print("Fin du Chapitre 4 très belle performance sur le terrain")
        afficher_maison_gagnante(maisons)
        afficher_personnage(joueur)


































