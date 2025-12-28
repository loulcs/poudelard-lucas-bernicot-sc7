import json
from symbol import continue_stmt

from utils.input_utils import demander_nombre
from utils.input_utils import demander_choix



def creer_equipe(maison,equipe_data,est_joueur=False,joueur=None):
    equipe = {"nom": maison,'score': 0,'a_marque': 0,'a_stoppe': 0, 'attrape_vifdor': False,'joueurs': equipe_data}
    if est_joueur==True and joueur==None:
        nouveau_joueurs=[joueur]
        for elem in equipe_data:
            if elem!=joueur:
                 nouveau_joueurs.append(elem)
        equipe['joueurs'] = nouveau_joueurs
    return equipe

import random
def tentative_marque(equipe_attaque,equipe_defense,joueur_est_joueur=False):
    proba_but=demander_nombre("Choississez un nombre:",1,10)
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
    nombre = demander_nombre("Choisissez un nombre:",1,6)
    if nombre==6:
        vifdor=True
    return vifdor

def attraper_vifdor(e1,e2):
    equipe_gagnante=demander_choix('Choissisez une equipe',[e1,e2])
    if equipe_gagnante == e1:
        e1['attrape_vifdor'] = True
        e1['score']+=150
    else:
        e2['attrape_vifdor'] = True
        e2['score']+=150
    return equipe_gagnante

def afficher_score(e1,e2):
    print("Score actuel:")
    tentative_marque(e1,e2,True)
    points=e2['score']
    points2=e1['score']
    print(e1['nom'],":",points2,"points",'\n',e2['nom'],":",points,"points")

def afficher_equipe(maison,equipe):
    print("Equipe de",maison,":")
    equipe_joueur = '\n''- '.join(equipe['joueurs'])
    return (equipe_joueur)


def match_quidditch(joueur,maisons):
    with open ('data/equipes_quidditch.json','r',encoding="utf-8")as f:
        equipe=json.load(f)
        maison_joueur=joueur[maisons]
        maison_adverse = demander_choix("Choisissez une maison",['Gryfondor','Serpentard','Serdaigle','Pouffsouffle'])
        print("Match de Quidditch:", maison_joueur, "vs", maison_adverse, "!")
        equipe_joueur= (creer_equipe(maison_joueur,equipe['joueurs'],est_joueur=False,joueur=None))
        equipe_adverse=(creer_equipe(maison_adverse,equipe['joueurs'],est_joueur=False,joueur=None))
        print(equipe_joueur)
        print(equipe_adverse)
        print(afficher_equipe(maison_joueur,equipe_joueur))
        print()
        print(afficher_equipe(maison_adverse,equipe_adverse))
        print("tu joue pour",equipe_joueur,"en tant qu'Attrapeur")
        i=0
        if i <20:
            tentative_marque(equipe_joueur,equipe_adverse,False)
            print(afficher_score(equipe_joueur,equipe_adverse))
            if apparition_vifdor():
                if attraper_vifdor(equipe_joueur,equipe_adverse)==maison_joueur:
                    equipe_joueur['score']+=150
            print("Le match est terminé")

        input("appuyer sur entrer pour continuer")
        i=i+1
        if i ==20:
            print(afficher_score(equipe_joueur,equipe_adverse))
            if equipe_joueur['score']>equipe_adverse['score']:
                print("La maison gagante est ",maison_joueur)
                print("Le match est remporté par",maison_joueur,"plus 500 points")
            elif equipe_adverse['score']>equipe_adverse['score']:
                print("La maison gagante est ",maison_adverse)
                print("Le match est remporté par",maison_adverse,"plus 500 points")
            else:
                print("Le match est nulle les deux equipes ont très bien joue")









































