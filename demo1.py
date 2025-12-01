with open("Magasin/produits.txt", "r") as fichier:
    contenu = fichier.read().splitlines()

print("Produits :")
print(contenu)

with open("Magasin/demo_liste.txt", "r") as fichier:
    fruits = fichier.read().split(",")

print("Fruits :")
print(fruits)

with open("demo_dict.txt", "r") as fichier:
    contenu = fichier.read().splitlines()

print("Capitales :")
print(contenu)
capitales = {}
for c in contenu:
    list_c = c.split(":")
    capitales[list_c[0]] = list_c[1]
print(capitales)

with open("Magasin/prix.csv", "r") as fichier:
    contenu = fichier.read().splitlines()

print("Prix :")
print(contenu)
prix = {}
for i in range(1, len(contenu)):
    list_p = contenu[i].split(",")
    prix[list_p[0]] = float(list_p[1])
print(prix)
ls_prix = list(prix.values())
total = sum(ls_prix)
print(total)