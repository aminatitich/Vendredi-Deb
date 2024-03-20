essaies = 6

def play(mot):

    print("Jouons au pendu!")
    mot_complet = "_"*len(mot)
    print(mot_complet)
    guessed_lettres = []
    guessed_mots = []
    guessed = False

    while essaies>0 and guessed == True:
        guess = str(input("Veuillez saisir une lettre ou un mot: "))