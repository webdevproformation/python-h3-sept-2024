# normalement lorsque vous installez python
# python l'interpréteur qui est installé
# pip Package Installer for Python
# pip --version

# pypi.org

# cd jour04
# pip install fr-date

from fr_date import conv
from  datetime import  datetime

date_naissance = "1975-01-01"
aujourdhui = datetime.today()

print(conv(date_naissance))
print(aujourdhui)
print(conv(aujourdhui))

# cas pratique
# trouver un module qui permet de utiliser l'algorithme de cryptage bcrypt()
# utiliser cet algorithme dans un fichier python de votre choix 