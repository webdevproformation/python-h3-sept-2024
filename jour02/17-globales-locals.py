import pprint

a = 10

pprint.pp(globals())

def traitement():
    pprint.pp(locals()) # {}

traitement() # système d'héritage objet local 
             # => objet englobant globals()
             # pprint.pp(vars(buildins))