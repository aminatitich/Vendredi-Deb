import random
nombre_secret = random.randint(1,100)

nombre = 0
count = 0

while nombre != nombre_secret:
    nombre = int(input("Veuillez saisir votre nombre: "))
    if nombre < nombre_secret:
        print("Trop basse!")
    elif nombre > nombre_secret:
        print("Trop elevée!")
    else:
        print("Bonne réponse, bravo!")

    count+=1

print(f"Vous avez essayer {count} fois! ")

