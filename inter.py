import os
with open("C:/Users/Amina TITICH/Desktop/DESKTOOP/Sample_texte.txt", "r") as file:
    texte = file.read()
    dict = {}
    for mot in texte:
        mots = texte.split()
        for i in mots:
            liste = i.strip(".,")
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    print(dict)