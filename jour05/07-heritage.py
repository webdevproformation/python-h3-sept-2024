
class A:
    def test(self):
        return "je suis la méthode test dans A"
    
# extends  pour faire hériter une class depuis une autre
# en PHP en Javascript et Java 
# en Python il n'y a pas le mot clé extends 
# on utilise en général ce mot clé 

class B(A):
    pass 

b = B() 
print(b.test()) # b 

# A class Parent Mère Père   class
# B class Enfant  Fille Fils sub class

# B class
# A class supérieur => super()


# Polymorphisme 

# traitement dans la class parent 
# traitement dans la class enfant qui vont la modifier 


class Humain:
    def __init__(self) -> None:
       print("je fais un print")

    def recupererNom(self):
        return 'voici le nom de l\'humain'
    
    def test(self):
        return "test"
    
class Etudiant(Humain):

    def __init__(self) -> None:
       # super().__init__()
       # Humain.__init__(self)
       print("je fais un print dans l'enfant")

    def recupererNom(self):
        # exécuter la méthode de la class supérieur 
        texte = super().recupererNom()
        print(texte)
        return 'voici le nom de l\'étudiant'
    
    def test(self):
        return "override" # outrepasser


e = Etudiant()
print(e.recupererNom())

"""
créer un fichier 08-exo.py

créer plusieurs class Article
titre
contenu
dt_creation

méthode genererHTML(){
return le html suivant
<article>
<h2>titre</h2>
<p>contenu</p>
<p>date de création : dt_creation </p>
</article>
}

class ArticleTechnique hérite de Article
définir les valeurs de 3 propriétés 
titre "Article technique"
contenu "lorem ipsum"
dt_creation => date aujourd'hui au format jj/mm/aaaa


class ArticleUne hérite de Article
redéfinir public méthode genererHTML(){
modifier les valeurs des 3 propriétés 
return le html suivant
<article class="article-une">
<h2>titre</h2>
<p>date de création : dt_creation </p>
</article>
}

"""
