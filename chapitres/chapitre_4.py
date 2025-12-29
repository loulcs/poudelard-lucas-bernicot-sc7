import json
from utils.input_utils import demander_nombre
from utils.input_utils import demander_choix



def creer_equipe(maison,equipe_data,est_joueur=False,joueur=None):
    equipe = {"nom": maison,'score': 0,'a_marque': 0,'a_stoppe': 0, 'attrape_vifdor': False,'joueurs': equipe_data['joueurs']}
    if est_joueur==True and joueur==None:
        nouveau_joueurs=[]
        for elem in equipe_data['joueurs']:
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
    point_actuel=e1['score']
    point_actuels=e2['score']
    print(e1['nom'],":",point_actuel,"points",'\n',e2['nom'],":",point_actuels,"points")

def afficher_equipe(maison,equipe):
    print("Equipe de",maison,":")
    equipe_joueur = '\n''- '.join(equipe['joueurs'])
    return (equipe_joueur)


def match_quidditch(joueur,maisons):
    with open ('data/equipe_quidditch.json','r')as f:
        equipe=json.load(f)
        maison_joueurs=joueur["Maison"]
        maison_adverse = demander_choix("Choisissez une maison",['Gryfondor','Serpentard','Serdaigle','Pouffsouffle'])
        equipe_joueur = creer_equipe(maison_joueurs,equipe['joueur'],False,None)
        equipe_adverse = creer_equipe(maison_adverse,equipe['joueur'],False,None)
        print(afficher_equipe(equipe_joueur,equipe_adverse))
        Tour=0
        while Tour<20:
            afficher_score(equipe_joueur,maison_joueurs)
            tentative_marque(equipe_adverse,maison_joueurs,True)
            tentative_marque(equipe_joueur,maison_joueurs,False)
            if apparition_vifdor()==True:
                print("Le match est terminé")
                break
            input("apuyer sur entrer pour continuer")
            Tour+=1
        afficher_score(equipe_joueur,maison_joueurs)

































