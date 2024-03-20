import random

nombre_secret = random.randint(1,10)

tentative = 2

i = 0

while i < tentative:

    nombre = int(input("Veuillez saisir un nombre: "))

    if 1 <= nombre <= 10:
        i+=1

        if nombre == nombre_secret:
            print("Vous avez devinez le nombre secret")
            break
        elif nombre < nombre_secret:
            print("Le nombre cherché est plus grand !!", tentative-i)
        else:
            print("Le nombre cherché est plus petit !!", tentative-i)

    else:
        print("Veuillez saisir un autre nombre entre 1 et 10")

if i == tentative and nombre != nombre_secret:
    print("Vous avez depassé les tentatives possible")        