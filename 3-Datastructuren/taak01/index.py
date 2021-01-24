Klas3C = (("Trevor", 18, "Amstelveen"),("George", 24,"Amsterdam"),("Bob", 17, "Aalsmeer"),("Alice",18, "Amsterdam"),("Johan", 20, "Uithoorn"),("Willemien",18, "Amsterdam"))
for naam,leeftijd,stad in sorted(Klas3C, key=lambda x: x[1]):
    print('Leerling naam is {}, Leerling leeftijd is {} en woont in {} '.format(naam,leeftijd,stad))
    