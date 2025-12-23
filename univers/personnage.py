def initialiser_personnage(nom, prenom, attributs):
    joueur={
    "Nom":nom,
    "Prenom": prenom,
    "Argent": 100,
    "Inventaire":[],
    "Sortilèges": [],
    "Attributs": attributs}
    return joueur

def modifier_argent(joueur, montant):
    joueur["Argent"] += montant
    return joueur

def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
    return joueur


def afficher_personnage(joueur):
    print("Profil du personnage:")
    for i in joueur:
        print(i,end=':')
        if type(elem)==list:
            for j in joueur[i]:
                print(','.join(joueur[i]))
        elif type(elem)==dict:
            print("")
            for elem in joueur[i]:
                print('-',elem,":",joueur[i][elem])
        else:
            print(i,":",joueur[i])














