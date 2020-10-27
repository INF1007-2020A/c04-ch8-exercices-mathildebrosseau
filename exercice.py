#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici

def premiere_difference(fichier1, fichier2):
    with open(fichier1, 'r', encoding='utf-8') as f1, open(fichier2, 'r', encoding='utf-8') as f2:
        for index, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                print(f"Les fichiers sont différents. À la ligne {index + 1}, on a: ", line1, "versus: ", line2)
                break

def triple_espace(fichier, fichier_copie):
    with open(fichier, 'r', encoding="utf-8") as original, open(fichier_copie, 'w', encoding='utf-8') as copie:
        for ligne_originale in original:
            copie.write(ligne_originale.replace(' ', '   '))


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    premiere_difference(r"C:\Users\Mathi\Documents\GitHub\c04-ch8-exercices-mathildebrosseau\exemple.txt", r"./exemple2.txt")
    triple_espace(r"C:\Users\Mathi\Documents\GitHub\c04-ch8-exercices-mathildebrosseau\exemple.txt", r"./exemple2_copie.txt")
