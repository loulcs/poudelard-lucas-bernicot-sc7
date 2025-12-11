def demander_texte(message):
    texte=input(message).strip()
    while texte=="":
        texte=input(message).strip()
    return texte
def demander_nombre(message, min_val=None, max_val=None):
        valide=False
        while valide==False :
            val_input = input(message).strip()
            if val_input=="":
                print("Erreur : saisie vide")
                continue
            else:
                signe=1
                debut=0
                if val_input[0] == "-":
                    signe=-1
                    debut=1
                    if len(val_input)==1:
                        print("Erreur : saisie non valide")
                        continue
                est_chiffre=True
                for c in val_input[debut:]:
                    if c<"0" or c>"9":
                        print("Erreur : saisie non valide")
                        est_chiffre=False
                        break
                if not est_chiffre:
                    continue
                val=0
                for c in val_input[debut:]:
                    val=val*10+ (ord(c)-ord("0"))
                val*=signe
                if val<min_val and min_val is not None :
                    print("Erreur : saisie non valide")
                    continue
                if max_val is not None and val>max_val:
                    print("Erreur : saisie non valide")
                    continue
                return val

def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r",encoding='utf-8') as fichier:
        donnee=json.load(fichier)
    return donnee

def demander_choix(message, options):
    print(message)



    for i in range(len(options)):
        print(i + ". " + options[i])
    choix = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix - 1]









