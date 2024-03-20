import random

def mot_obtenu():
    with open("file.txt","r") as mon_fichier:
        liste = mon_fichier.read().splitlines()
        mot = random.choice(liste)
    return mot.upper()

print(mot_obtenu())
def afficher_pendu(essaies):
    phases = [
                """
                   --------
                   |      |
                   |      O
                   |    \ | /
                   |      |
                   |     / \
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    \ | /
                   |      |
                   |     
                   -
                """,
                 """
                   --------
                   |      |
                   |      O
                   |    \ | /
                   |      
                   |     
                   -
                """,
                 """
                   --------
                   |      |
                   |      O
                   |    \ | 
                   |      
                   |     
                   -
                """,
                  """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                 """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """ ]
    return phases[essaies]

def play(mot):
    mot_complet = "_" * len(mot)
    guessed_lettres = []
    guessed_mots = []
    essais = 5
    guessed = False

    print("Jouons au pendu !")

    print(afficher_pendu(essais))

    print(mot_complet)

    print("\n")

    while guessed == False and essais > 0:
        guess = str(input("Veuillez saisir une lettre ou un mot: ")).upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_lettres:
                print("Vous avez deja deviné cettre lettre!")

            elif guess not in mot:
                print(f"{guess} n'est pas dans le mot")
                guessed_lettres.append(guess)
                essais -= 1
            else:
                print(f"Bravo, {guess} est dans le mot")
                
                guessed_lettres.append(guess)

                mot_liste = list(mot_complet)

                indice = []
                for i in range(len(mot)):
                    if mot[i] == guess:
                        indice.append(i)

                for j in indice:
                    mot_liste[j] = guess

                mot_complet = "".join(mot_liste)

                if "_" not in mot:
                    guessed = True


        elif len(guess) == len(mot) and guess.isalpha():

            if guess in guessed_mots:
                print("Vous avez deja deviné ce mot!")

            elif guess not in mot:
                print(f"{guess} n'est pas le mot")
                guessed_mots.append(guess)
                essais -= 1

            else:
                mot_complet = mot
                guessed = True
        else:
            print("Veuillez saisir une lettre ou un mot: ")


        print(afficher_pendu(essais))
        print(mot_complet)

    if guessed == True:
        print("Bravo, vous avez deviné le mot !")

    else:
        print("Dommage, vous avez epuisé tout les essais!, le mot était: ", mot)

        
def main():
    mot = mot_obtenu()
    play(mot)
    q = str(input("Voulez vous joué encore? (Y/N): ")).upper()
    if q == "Y":
        mot = mot_obtenu()
        play(mot)

        
if __name__ == "__main__":
    main()











"""
import os
with open("","r") as myfile:
    liste = myfile.read().strip()
    mot = random.choice(liste)

"""