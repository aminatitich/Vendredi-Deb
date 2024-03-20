import random

def mot_obtenu():
    with open("file.txt","r") as mon_fichier:
        liste = mon_fichier.read().splitlines()
        mot = random.choice(liste)
    return mot.upper()

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

                if "_" not in mot_complet:
                    guessed = True

        elif len(guess) == len(mot) and guess.isalpha():
            if guess in guessed_mots:
                print("You already guessed this word !")

            elif guess not in mot:
                essais -=1
                print(f"{guess} n'est pas le mot !")
                guessed_mots.append(guess)
            
            else:
                
                mot_complet = mot
                guessed = True
            
        else:
            print("Veuillez saisir une lettre ou un mot valide: ")


        print(afficher_pendu(essais))
        print(mot_complet)

    if guessed == True:
        print("Bravo! you guessed the word: " , mot)
    else:
        print("You lost, the word was: ", mot)

def main():
    mot = mot_obtenu()
    play(mot)
    playagain = input("Would you like to play again ? (Y or N)")
    if playagain == "y":
        play(mot)
    else:
        print("Ok, thank you for playing!")

main()







