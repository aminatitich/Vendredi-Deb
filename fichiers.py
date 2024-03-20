"""
Supposons que vous ayez un fichier nommé "scores.txt" avec le contenu suivant :

Alice 85
Bob 70
Charlie 90
Diana 65
Eva 75

L'exercice consiste à lire ce fichier, à calculer le score moyen 
et à identifier l'élève ayant le score le plus élevé.
"""








score = {}
total = 0

with open('scores.txt', 'r') as file:
    for line in file:
        name, score = line.strip().split()
        score[name] = int(score)
        total += int(score)


num_etudiants = len(score)
moyenne = total / num_etudiants if num_etudiants > 0 else 0


maximum = max(score.values())
top_etudiant = [nom for nom, s in score.items() if score == maximum]


print("Scores:")
for nom, score in score.items():
    print(f"{nom}: {score}")

print(f"\nLa moyenne: {moyenne:.2f}")

print("\nL'élève ayant obtenu le meilleur score :")
for etudiant in top_etudiant:
    print(f"{etudiant} scored the highest: {maximum}")
