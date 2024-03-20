import os
def freq_count(fichier_nom):
    with open(fichier_nom,"r") as file:
        dict = {}
        for ligne in file:
            mot = ligne.split()
            for i in mot:
                i = i.lower().strip(".,")
                if i not in dict:
                    dict[i]=1
                else:
                    dict[i]+=1

    for key, value in dict.items():
        print(f"{key}: {value}")

 


freq_count("C:/Users/Amina TITICH/Desktop/DESKTOOP/sample_texte.txt")
