import csv

produits = []
with open('Magasin/produits.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        produits.extend(row)
print(produits)

prix = []
with open('Magasin/prix.csv', 'r') as file:
    reader = csv.reader(file) #Comme une liste de listes
    for row in reader:
        if row[1] != 'Prix':
            prix.append(float(row[1]))
print(prix)
print(sum(prix))

dict_prix = {}
with open('Magasin/prix.csv', 'r') as file:
    dict_reader = csv.DictReader(file) #Comme une liste de dictionnaires
    for row in dict_reader:
        dict_prix[row["Produit"]] = float(row["Prix"])
print(dict_prix)
print(sum(dict_prix.values()))