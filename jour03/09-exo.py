employees = ['Corey', 'Jim' , 'Steven' , 'April' , 'Judy' , 'Jenn' , 'John' , 'Jane'] 
gym_members = ['April', 'John' , 'Corey']
developers = ['Judy' , 'Corey' , 'Steven' , 'Jane' , 'April']

# quels sont les utilisateurs qui sont developpers et sont inscrits au club de gym

dev_et_gym = set(gym_members).intersection(developers)
print(dev_et_gym) # {'Corey', 'April'}

# quels sont les utilisateurs qui ne sont ni developpers ni inscrits au club de gym

uniquement_employee = set(employees).difference(gym_members, developers)
print(uniquement_employee) # {'Jenn', 'Jim'}

# est ce que Steven est inscrit au club de gym ?

print ("Steven" in gym_members) # False