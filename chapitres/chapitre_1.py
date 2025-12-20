def introduction():
    print("Bienvenue dans le monde magique de Poudlard ! ")
    print("Vous êtes un jeune sorcier qui s'apprête à vivre sa première année à Poudlard.")
    print("Votre aventure commence maintenant !")

def cree_personnage(joueur):
    import random
    prenom = input("Entrez le prenom de votre personnage : ")
    nom = input("Entrez le nom de votre personnage : ")
    for elem in joueur["Attributs"].item():
        for cle in elem.keys():
         nombre = random.randint(1,10)
         joueur["Attributs"][cle] = nombre
         attribut = joueur["Attributs"]
    print(initialiser_personnage(nom,prenom,attribut))

