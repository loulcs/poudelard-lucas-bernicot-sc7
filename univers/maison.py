from utils.input_utils import demander_choix

def actualiser_points_maison(maisons, nom_maison, points):
    if not nom_maison in maisons:
      print('la maison ', nom_maison,  ' est introuvable')
      return
    if points>=0:
        print("Plus ", end='')
    else:
        print("Moins ", end='')
    maisons[nom_maison]+= points
    print(abs(points),"points pour",nom_maison,"!")
    print(' Nouveau total: ', maisons[nom_maison])
    return

def afficher_maison_gagnante(maisons):
    max=0
    gagnant=[]
    for nom in maisons:
        if maisons[nom]>max:
            max=maisons[nom]
    for nom in maisons:
        if maisons[nom]==max:
            gagnant.append(nom)
    if len(gagnant)>1:
        for g in gagnant:
            print("La maison en tête est{}".format(g))
import random
def repartition_maison(joueur,questions):
    dico_score={"Gryffondor":0, "Serpentard":0, "Poufsouffle":0, "Serdaigle":0}
    attribut=joueur["Attributs"]
    lien = {"courage":"Gryffondor","ambition":"Serpentard","loyauté": "Poufsouffle", "intelligence":"Serdaigle"}
    for elem in attribut :
        dico_score[lien[elem]]+=2*attribut[elem]
    for tuple in questions:
        reponse = demander_choix(tuple[0],tuple[1])
        indice = 0
        while tuple[1][indice]!=reponse:
            indice+=1
        dico_score[tuple[2][indice]]+=3
    score_max = 0
    for val in dico_score.values():
        if val>score_max:
            score_max=val
    maisons_choisi=[]
    for maison in dico_score:
        if dico_score[maison]==score_max:
            maisons_choisi.append(maison)
    if len(maisons_choisi)==1:
        return maisons_choisi[0]
    else:
        print("Hum, c'est difficile!Je vois du courage, de l'intelligence mais aussi de l'ambition...")
        maison_finale=random.choice(maisons_choisi)
        return maison_finale







