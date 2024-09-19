# pip install bcrypt
# https://pypi.org/project/bcrypt/

import bcrypt

password = b"azerty1234"

salt = bcrypt.gensalt()

# la fonction qui permet de hashé une string en hash => hashpw()
# password en clair en code en byte
# salt chaine de caractère alétoire qui est ajoutée au password 
# pour le rendre plus difficile à trouvé

""" passwordHasse = bcrypt.hashpw(password, salt)

print(passwordHasse)  """

# b'$2b$12$UlQ7Hfpgqbn1ULmSw/UndueC8f4zTykbj6D2IpUrv/EA8ISSBeHoC'
passwordHash =  b'$2b$12$KCM1PMQWo8HaVd0utSC/f.qBQZ9JMp6EJEFLV0vVwTbclSxCtfBpe'

verif =  bcrypt.checkpw( password  , passwordHash  )
print(verif)

# 5f4dcc3b5aa765d61d8327deb882cf99