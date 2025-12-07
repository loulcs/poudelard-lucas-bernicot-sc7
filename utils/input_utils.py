def demander_texte(message):
    texte=input(message).strip()
    while texte=="":
        texte=input(message).strip()
    return texte
def demander_nombre(message, min_val=None, max_val=None):
        val = input(message).strip())
        if min_val is None and max_val is None:
            return val
        elif min_val is not None and max_val is None :
            if val >= min_val :
                return val



