import pprint # pretty print 
import math  # fonction mathématique => cos tan pi e ...
import os    # accès à votre système exploitation => lancer de logiciel 
import datetime # date
import calendar # calendrier (mois / jour / année)
import inspect # version plus avancée pour débugger / suivre votre code pas à pas ... 
import tkinter # créer des UI directement disponible dans l'ordinateur 
import threading # ajouter de processus en + pour exécuter plus vite votre projet 
import time
import sqlite3

""" # pprint.pp(math.__dict__)
# pprint.pp(os.__dict__)
# pprint.pp(datetime.__dict__)
pprint.pp(calendar.__dict__) """

def allerEnCours():
    time.sleep(5)
    print("je vais en cours")

def dejeuner():
    time.sleep(2)
    print("je fini de manger")

thread1 = threading.Thread(target=allerEnCours)
thread1.start()
thread2 = threading.Thread(target=dejeuner)
thread2.start()

""" allerEnCours()
dejeuner() """

# cas pratique 
# créer un fichier dans le dossier en cours base.db (soit à la main ou via un script python)
# créer un autre fichier 06-exo.py 
# ce fichier va établir une connexion avec le fichier base.db via le module sqlite3
# créer une table exemple qui contient 3 colonnes 
# id clé primaire
# nom contient du texte
# dt_creation qui contient DATETIME

# insérer dans cette table les informations suivantes 
# 1 Alain 1988-01-02
# 2 Céline 2021-12-15