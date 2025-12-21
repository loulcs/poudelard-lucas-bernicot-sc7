from univers.personnage import afficher_personnage
from univers.personnage import initialiser_personnage
from utils.input_utils import demander_nombre
from utils.input_utils import demander_choix


def introduction():
    print("Bienvenue dans le monde magique de Poudlard ! ")
    print("Vous êtes un jeune sorcier qui s'apprête à vivre sa première année à Poudlard.")
    print("Votre aventure commence maintenant !")

def cree_personnage():
   prenom = input("Entrez le prenom de votre personnage : ")
   nom = input("Entrez le nom de votre personnage : ")
   attribut={"courage":0,"intelligence":0,"loyauté":0,"ambition":0}
   joueur=initialiser_personnage(nom, prenom, attribut)
   print("Choisissez vos attributs:")
   for elem in attribut:
       message="Choisissez votre niveau de"+ elem +"(1-10):"
       nombre = demander_nombre(message, 1, 10)
       joueur["Attributs"][elem] = nombre
       afficher_personnage(joueur)

def recevoir_lettre():
   print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard... ")
   input()
   print(""" Cher élève,
         Nous avons le plaisir de vous informer que vous avez été admis à l'école de sorcellerie de Poudlard ! """)
   reponse=demander_choix( "Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",["Oui, bien sûr !"," Non, je préfère rester avec l’oncle Vernon... "])
   if reponse!="Oui, bien sûr ! ":
       print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie:"
             "« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » "
             "Le monde magique ne saura jamais que vous existiez...")
       exit()

def renconter_hagrid(personnage):
   print(personnage+ 'Salut Harry ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.' )
   reponse=demander_choix("Voulez-vous suivre Hagrid ?",["Oui","Non"] )
   if reponse=="Non":
       print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")

