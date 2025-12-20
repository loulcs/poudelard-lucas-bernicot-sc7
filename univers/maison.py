def actualiser_points_maison(maisons, nom_maison, points):
    if points>=0:
        maisons[nom_maison]+= points
        print("Plus",points,"points pour",nom_maison,"!")
    else:
        maisons[nom_maison]-= points
        print("Moins", points, "points pour", nom_maison, "!")
    return maisons

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
            print(g,end="")
import random
def repartition_maison(joueur,questions):
    dico_score={"Gryffondor":0, "Serpentard":0, "Poufsouffle":0, "Serdaigle":0}
    attribut=joueur["Atrributs"]
    lien = {"Courage":"Gryffondor","Ambition":"Serpentard","Loyauté": "Poufsouffle", "Intelligence":"Serdaigle""}
    for elem in attribut :
        dico_score[lien[elem]]+=2*attribut[elem]
    indice=0
    for tuples in questions:
        reponse = demander_choix(tuples[0],tuples[1])
        while tuples[1][indice]!=reponse:
            indice+=1
        dico_score[tuples[2][indice]]+=3
    score_max = 0
    for val in dico_score.values():
        if val>score_max:
            score_max=val
    maisons_choisi=[]
    for maison in dico_score:
        if dico_score[maison]==score_max:
            maisons_choisi.append(maison)
    if len(maisons_choisi)=1:
        return maisons_choisi[0]
    else:
        print("Hum, c'est difficile!Je vois du courage, de l'intelligence mais aussi de l'ambition..."
        maison_finale=random.choice(maisons_choisi)
        return maison_finale







