Projet Python Poudelard

Jeu créé en python qui reproduit l'univers d'Harry Potter en plongeant le joueur lors de sa première année à Poudelard.

Contributeurs :Lou Lucas SC7 , Camille Bernicot BN

Installation  du jeu: Lancer le jeu :  run main.py

Fonctionnalités Principales : 

-création du personnage du joueur

-création de l'univers d'Harry Potter 

-choix et gestion de la maison du joueur

-apprentissage aléatoire de sorts (offensifs, défensifs et utilitaires)

-quiz de magie avec attribution de points à la maison

-simulation d’un match de Quidditch

-gestion des scores des maisons

-affichage des informations du joueur

Journal de Bord 
->Chronologie du Projet :
SEMAINE 1 : Création du projet sur pycharm / git hub, création de l'arborescence demandée, remplissage fichier json
  -> peu d'avancement car problème avec push/pull et problème d'affichage
SEMAINE 2 : Implémentation utils/input_utils.py,univers/personnage.py, chapitres/chapitre_1.py 
SEMAINE 3 : Implémentation  menu.py,univers/maison.py,chapitres/chapitre_2.py 
SEMAINE 4 : Implémentation chapitre 3 , chapitre 4 , readme , dépot final, tests


-> Répartition des Tâches :

  Input_utils 
  
    Demander texte : Lou
    Demander nombre : Lou 
    Load-fichier : Lou
    Demander choix : Camille 
  Personnage
  
    Initialiser personnage : Lou
    Modifier argent , ajouter objet : Lou
    Afficher personnage : Camille 
    Actualiser point maison : Camille 
    Afficher maison gagnante :Lou
    Répartition maison :Camille 
  Chapitre 1 :
  
    introduction,créer personnage ,recevoir lettre : Camille 
    Rencontrer hagrid,acheter fournitures,lancer chapitre 1 : Lou 
  Chapitre 2 : Lou 
  
  Chapitre 3 : Lou 
  
  Chapitre 4 : Camille 
  
  Menu : Camille 

Contrôle, Tests et Validation :
Menu principal

Affichage :

Lancer le Chapitre 1 - L'arrivée dans le monde magique.

Quitter le jeu.
Appuyez sur ENTREE pour continuer...

Affichage :
Que voulez vous faire ?
1 . 1
2 . 2

Saisie utilisateur : 1

Création du personnage

Affichage :
Bienvenue dans le monde magique de Poudlard !
Vous êtes un jeune sorcier qui s'apprête à vivre sa première année à Poudlard.
Votre aventure commence maintenant !

Affichage : Entrez le prénom de votre personnage :
Saisie utilisateur : Lou

Affichage : Entrez le nom de votre personnage :
Saisie utilisateur : Lucas

Affichage :
Choisissez votre niveau de courage (1-10) :
Saisie utilisateur : 4

Affichage :
Choisissez votre niveau de intelligence (1-10) :
Saisie utilisateur : 5

Affichage :
Choisissez votre niveau de loyauté (1-10) :
Saisie utilisateur : 7

Affichage :
Choisissez votre niveau de ambition (1-10) :
Saisie utilisateur : 3

Affichage :
Profil du personnage :
Nom : Lucas
Prenom : Lou
Argent : 100
Inventaire :
Sortilèges :
Attributs :

courage : 4

intelligence : 5

loyauté : 7

ambition : 3

Lettre de Poudlard

Affichage :
Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...
Appuyez sur ENTREE pour ouvrir la lettre

Saisie utilisateur : ENTREE

Affichage :
Souhaitez-vous accepter cette invitation et partir pour Poudlard ?
1 . Oui, bien sûr !
2 . Non, je préfère rester avec l’oncle Vernon...

Saisie utilisateur : 1

Chemin de Traverse

Affichage :
Hagrid : Salut Lou ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.
Voulez-vous suivre Hagrid ?
1 . Oui
2 . Non

Saisie utilisateur : 1

Affichage :
Catalogue des objets disponibles :
Vous avez 100 galions.

Saisie utilisateur : 1
Affichage : Vous avez acheté : Baguette magique (-35 galions).

Saisie utilisateur : 2
Affichage : Vous avez acheté : Robe de sorcier (-20 galions).

Saisie utilisateur : 4
Affichage : Vous avez acheté : Manuel de potions (-25 galions).

Affichage :
Voici les animaux disponibles :

Saisie utilisateur : 2
Affichage : Vous avez choisi : Chat (-15 galions)

Chapitre 2 – Choixpeau

Affichage :
Que répondez-vous à Ron ?
Saisie utilisateur : 1

Affichage :
Que répondez-vous à Hermione ?
Saisie utilisateur : 1

Affichage :
Comment réagissez-vous face à Drago ?
Saisie utilisateur : 3

Affichage :
Tes attributs mis à jour :
courage : 5
intelligence : 6
loyauté : 8
ambition : 3

Affichage :
Le Choixpeau magique t’observe longuement.

Affichage :
Tu vois un ami en danger. Que fais-tu ?
Saisie utilisateur : 4

Affichage :
Quel trait te décrit le mieux ?
Saisie utilisateur : 4

Affichage :
Face à un défi difficile, tu...
Saisie utilisateur : 3

Affichage :
Le Choixpeau s’exclame : Poufsouffle !!!

Chapitre 3 – Quiz

Affichage :
Question 1 :
Saisie utilisateur : Veritas

Affichage :
Question 2 :
Saisie utilisateur : Boum

Affichage :
Question 3 :
Saisie utilisateur : Silencio

Affichage :
Question 4 :
Saisie utilisateur : Smokey

Affichage :
Score obtenu : 25 points

Chapitre 4 – Quidditch
Affichage :
Match de Quidditch : Gryffondor vs Serdaigle !

Affichage :
Tu joues pour Gryffondor en tant qu’Attrapeur.

━━━ Tour 1 ━━━

Affichage :
Serdaigle attaque…
Gryffondor bloque l’attaque !

Affichage :
Gryffondor attaque…
Serdaigle bloque l’attaque !

Affichage :
Score actuel :
→ Gryffondor : 0 points
→ Serdaigle : 0 points

Affichage :
Le Vif d’Or n’apparaît pas.

Affichage :
Appuyez sur Entrée pour continuer
Saisie utilisateur : ENTREE

━━━ Tour 2 ━━━

Affichage :
Harry Potter (Attrapeur) marque un but pour Gryffondor ! (+10 points)

Affichage :
Serdaigle attaque…
Gryffondor bloque l’attaque !

Affichage :
Score actuel :
→ Gryffondor : 10 points
→ Serdaigle : 0 points

Affichage :
Le Vif d’Or n’apparaît pas.

Affichage :
Appuyez sur Entrée pour continuer
Saisie utilisateur : ENTREE

━━━ Tour 3 ━━━

Affichage :
Serdaigle marque un but ! (+10 points)

Affichage :
Gryffondor attaque…
Serdaigle bloque l’attaque !

Affichage :
Score actuel :
→ Gryffondor : 10 points
→ Serdaigle : 10 points

Affichage :
Le Vif d’Or n’apparaît pas.

Affichage :
Appuyez sur Entrée pour continuer
Saisie utilisateur : ENTREE

━━━ Tour 4 ━━━

Affichage :
Harry Potter (Attrapeur) marque un but pour Gryffondor ! (+10 points)

Affichage :
Serdaigle attaque…
Gryffondor bloque l’attaque !

Affichage :
Score actuel :
→ Gryffondor : 20 points
→ Serdaigle : 10 points

Affichage :
Le Vif d’Or n’apparaît pas.

Affichage :
Appuyez sur Entrée pour continuer
Saisie utilisateur : ENTREE

━━━ Tour 5 ━━━

Affichage :
Serdaigle attaque…
Serdaigle marque un but ! (+10 points)

Affichage :
Gryffondor attaque…
Serdaigle bloque l’attaque !

Affichage :
Score actuel :
→ Gryffondor : 20 points
→ Serdaigle : 20 points

Affichage :
 Le Vif d’Or apparaît ! 

Affichage :
Le Vif d’Or a été attrapé par Serdaigle ! (+150 points)

Fin du match

Affichage :
Fin du match !

Affichage :
Score final :
→ Gryffondor : 20 points
→ Serdaigle : 170 points

Affichage :
Résultat final :
Le Vif d’Or a été attrapé par Serdaigle !
+150 points pour Serdaigle ! Total : 170 points.

Affichage :
Serdaigle remporte le match !
+500 points pour Serdaigle !

Affichage :
Total maison Serdaigle : 670 points
Fin du Chapitre 4
Félicitations, vous avez terminé votre aventure à Poudlard 



