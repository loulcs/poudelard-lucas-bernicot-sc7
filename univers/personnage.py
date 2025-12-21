def initialiser_personnage(nom, prenom, attributs):
    joueur={
    "Nom":nom,
    "Prenom": prenom,
    "Argent": 100,
    "Inventaire":[],
    "Sortilèges": [],
    "Attributs": attributs}
    return dico_perso

def modifier_argent(joueur, montant):
    joueur["Argent"] += montant
    return joueur

def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
    return joueur


def afficher_personnage(joueur):
    print("Profil du personnage:")
    for i in joueur:
        if isinstance(joueur[i], list):
            for j in joueur[i]:
                print(j,end='')
        elif isinstance(joueur[i], dict):
            for elem in joueur[i]:
                print(elem,":",joueur[i][elem])
        else:
            print(i,":",joueur[i])














