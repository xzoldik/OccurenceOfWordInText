import time
import random
import os
import matplotlib.pyplot as plt

les_tailles = [10, 100, 1000, 10000, 100000, 1000000]
def generer_un_mot():
    mot = ""
    nombre_de_lettre = random.randint(1, 10)
    for _ in range(nombre_de_lettre):
        letter_ascii = random.randint(97, 122)
        mot += chr(letter_ascii)
    return mot + " "
def generer_une_ligne():
    ligne = ""
    nombre_de_mot = random.randint(1, 20)
    for _ in range(nombre_de_mot):
        ligne += generer_un_mot()
    return ligne + " "


def generer_paragraphe(nombre_de_ligne):
    paragraphe = ""
    for _ in range(nombre_de_ligne):
        paragraphe += generer_une_ligne() + "\n"
    return paragraphe


def generer_texte():
    with open('data.txt', 'w') as file:
        for taille in les_tailles:
            file.write(str(taille))
            file.write("\n")
            file.write(generer_paragraphe(taille))


def creation_de_text_dans_un_fichier():
    try:
        if os.path.exists("data.txt") == 0 or os.stat("data.txt").st_size == 0:
            generer_texte()
        else:
            print("le fichier n'est pas vide")
    except:
        print("le fichier pas trouver")

def calculer_le_nombre_doccurences_dun_mot(mot):
    table_de_temps = []
    nombre_de_repetition = 1
    with open('data.txt', 'r') as file:
        position_actuelle = 0
        for taille in les_tailles:
            counteur = 0
            resultat = 0
            for _ in range(nombre_de_repetition):
                file.seek(position_actuelle)  # Set file pointer to the previous position
                lines = file.readlines()[position_actuelle + 1:taille + 1]  # Read only the relevant lines
                # Get the current position after reading lines
                debut = time.time()
                for line in lines:
                    mots = line.split()
                    for j in mots:
                        if j == mot:
                            counteur += 1
                fin = time.time()
                resultat += fin - debut
            le_temps_moyen = resultat / nombre_de_repetition
            table_de_temps.append(le_temps_moyen)
            position_actuelle = taille + 1
        return table_de_temps



def traçage_courbe():
    creation_de_text_dans_un_fichier()
    mot_a_rechercher = generer_un_mot()
    tableau_de_temps_de_recherche = calculer_le_nombre_doccurences_dun_mot(mot_a_rechercher)
    plt.plot(les_tailles, tableau_de_temps_de_recherche, label="Le temps De Recherche de nombre d'occurences")
    plt.xlabel("Taille")
    plt.ylabel("Temps Moyen (seconds)")
    plt.title(f"temps De Recherche de nombre d'occurences '{mot_a_rechercher}'")
    plt.legend()
    plt.show()

traçage_courbe()
