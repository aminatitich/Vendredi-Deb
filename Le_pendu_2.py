import tkinter as tk
import random

mot_secret = ""
mot_affiche = []
lettres_utilisees = []
nb_erreurs_max = 6
nb_erreurs = 0

def nouvelle_partie():
    global mot_secret, mot_affiche, lettres_utilisees, nb_erreurs
    mot_secret = mots[random.randint(0, len(mots) - 1)].upper()
    mot_affiche = ['_'] * len(mot_secret)
    lettres_utilisees = []
    nb_erreurs = 0
    afficher_mot()
    afficher_pendu()

def deviner_lettre():
    global nb_erreurs
    lettre = lettre_entree.get().upper()
    if lettre not in lettres_utilisees:
        lettres_utilisees.append(lettre)
        if lettre in mot_secret:
            for i in range(len(mot_secret)):
                if mot_secret[i] == lettre:
                    mot_affiche[i] = lettre
            afficher_mot()
            if '_' not in mot_affiche:
                resultat_label.config(text="Vous avez gagné!")
                nouvelle_partie()
        else:
            nb_erreurs += 1
            afficher_pendu()
            if nb_erreurs >= nb_erreurs_max:
                resultat_label.config(text=f"Vous avez perdu! Le mot était {mot_secret}")
                nouvelle_partie()
                
    lettre_entree.delete(0,tk.END)

def afficher_mot():
    mot_label.config(text=' '.join(mot_affiche))

def afficher_pendu():
    erreur_label.config(text=f"Erreurs: {nb_erreurs}/{nb_erreurs_max}")

mots = ["PYTHON", "JAVA", "JAVASCRIPT", "HTML", "CSS", "RUBY", "PHP"]

root = tk.Tk()
root.title("Jeu du Pendu")

# Interface graphique
mot_label = tk.Label(root, text="", font=("Helvetica", 16))
mot_label.pack()

lettre_entree = tk.Entry(root, width=5, font=("Helvetica", 16))
lettre_entree.pack()

deviner_bouton = tk.Button(root, text="Deviner", command=deviner_lettre, font=("Helvetica", 16))
deviner_bouton.pack()

erreur_label = tk.Label(root, text="", font=("Helvetica", 16))
erreur_label.pack()

resultat_label = tk.Label(root, text="", font=("Helvetica", 16))
resultat_label.pack()

nouvelle_partie()

root.mainloop()
