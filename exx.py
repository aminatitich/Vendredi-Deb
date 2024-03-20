import random
choix_ordinateur = random.choice(["Pierre","Feuil","Ciseaux"])

while True:
    mon_choix = str(input("Veuillez saisir: Pierre, Feuil ou Ciseaux  "))

    if choix_ordinateur == mon_choix:
        print("Egalité!")

    elif choix_ordinateur == "Pierre" and mon_choix == "Ciseaux":
        print("Vous avez perdu.")

    elif choix_ordinateur == "Feuil" and mon_choix == "Pierre":
        print("Vous avez perdu.")

    elif choix_ordinateur == "Ciseaux" and mon_choix == "Feuil":
        print("Vous avez perdu.")

    else:
        print("Vous avez gagné!")

    question = str(input("Vous voulez jouer encore? (Y/N): "))
    if question == "Y":
        continue
    if question == "N":
        break
    else:
        print("Saisir soit Y ou N !!")



