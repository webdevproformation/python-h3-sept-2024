def bonjour(f):
    def wrapper():
        print("bonjour")
        f()
    return wrapper

def identifiant(f):
    def wrapper():
        id = input("veuillez saisir votre identifiant ? \n")
        if id == "10" :
            f()
        else:
            print("identifiants invalides")
    return wrapper 

@bonjour
@identifiant
def login():
    print("bienvenue dans l'espace de gestion")

login()