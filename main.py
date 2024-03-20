import random 

def mot_obtenu():
    liste = ["Robot", "Programmation", "Pytho,", "Ordinateur","AI", "Java", "IT", "Computer Science"]
    mot = random.choice(liste)
    return mot

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


    essaies = 8
    print("Jouons au pendu")
    print(afficher_pendu(essaies))
    mot_complet = "_"*len(mot)
    guessed = True

    guessed_mot = []
    guessed_lettres = []


    print(mot_complet)

    while essaies > 0 and guessed == False:
        guess = str(input("Veuillez saisir une lettre ou un mot: "))
        if len(guess) == 1:
            
        


