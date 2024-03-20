"""Créez un programme qui joue à un jeu de pierre, papier, ciseaux contre l'utilisateur.

Pour ce faire, vous devrez utiliser une boucle pour permettre à l'utilisateur de jouer 
plusieurs tours de jeu. Vous devrez également utiliser des conditions pour déterminer 
le résultat de chaque tour en fonction des règles du jeu de pierre, papier, ciseaux."""

#import random

#choice_computer = random.choice(["Rock", "Scissor", "Paper"])

import random


hc=str(input("Choisissez entre pierre feuille ou ciseaux pour jouer contre le bot!"))

bc=""

y= random.randint(1,3)


if y == 1:

    bc="pierre"

elif y == 2:

    bc="feuille"

else:

    bc="ciseaux"


if hc == bc:

    print("Match nul!, j'ai choisit: ", bc)

elif hc == "pierre" and bc=="feuille" or hc =="feuille" and bc=="ciseaux" or hc=="ciseaux" and bc=="pierre":

    print( "J'ai gagné!, j'ai choisit: ", bc)

else:

    print( "Vous avez gagné!, j'ai choisit: ", bc)