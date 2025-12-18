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

def