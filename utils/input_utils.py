def demander_texte(message):
    texte=input(message)
    while texte==" ":
        texte=input(message)
    return texte
def demander_nombre(message, min_val=None, max_val=None):