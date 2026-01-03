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
        elem = joueur[i]
        print(i,end=':')
        if type(elem)==list:
                print(','.join(joueur[i]))
        elif type(elem)==dict:
            print("")
            for souselem in elem :
                print('-',souselem,":",elem[souselem])
        else:
            print(elem)














