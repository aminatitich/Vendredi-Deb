import random

def jeu(): 

    mon_fichier= open("file.txt","r")

    liste = mon_fichier.read().splitlines()

    mot = random.choice(liste).upper()

    mot_complet = "_" * len(mot)

    guessed_lettres = []

    guessed_mots = []

    essais = 5

    guessed = False

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


    while guessed == False and essais > 0:

        guess = str(input("Veuillez saisir une lettre ou un mot: ")).upper()

        print(phases[essais])

        if len(guess) == 1 and guess.isalpha():

            if guess in guessed_lettres:

                print("Vous avez deja deviné cettre lettre!")


            elif guess not in mot:

                

                print(f"{guess} n'est pas dans le mot")

                guessed_lettres.append(guess)

                essais -= 1


            else:

                print(phases[essais])

                print(f"Bravo, {guess} est dans le mot")

                

                guessed_lettres.append(guess)


                mot_liste = list(mot_complet)


                indice = []

                for i in mot:

                    if mot[i] == guess:

                        indice.append(i)


                for j in indice:

                    mot_liste[j] = guess


                mot_complet = "".join(mot_liste)

                if "_" not in mot_complet:
                    guessed = True




        elif len(guess) == len(mot) and guess.isalpha():

            if guess in guessed_mots:

                print("Vous avez deja deviné ce mot!")


            elif guess is not mot:

                print(f"{guess} n'est pas le mot")

                guessed_mots.append(guess)

                essais -= 1

            else:

                guessed = True
                
                mot_complet = mot

        if guessed == True:
            print()        

        

        else:

            print("veuillez mettre un mot vallide")

jeu()