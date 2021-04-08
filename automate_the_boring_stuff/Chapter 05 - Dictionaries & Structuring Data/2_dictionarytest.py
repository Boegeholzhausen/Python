profil = {'name': 'Jannis', 'age': 27}
profil['Job'] = "Ingenieur"
profil['name'] = "Jannis Bögeholz"


if 'name' and 'age' in profil.keys():
    print("yes")

print(profil)

for i in profil.values():
    print(i)

for i in profil.keys():
    print(i)

for i in profil.items():
    print(i)

print(str(profil.get('name', 'not exists')))