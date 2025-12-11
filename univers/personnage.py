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

