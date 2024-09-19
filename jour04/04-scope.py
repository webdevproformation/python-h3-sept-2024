class A:
    prop = 10 # public
    _protected = 20 # protected
    __private = 30  # __private 
    # convention de nommage des propriétés 

a = A()

print(a.prop) # 10
a.prop = 30
print(a.prop) # 30

## Name Mangling => bidouiller le nom

# print(a.__private) # AttributeError: 'A' object has no attribute '__private'. Did you mean: '_A__private'?

print(a._A__private)

a._A__private = 99

print(a._A__private)