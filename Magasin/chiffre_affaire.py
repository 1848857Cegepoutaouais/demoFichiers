import json
import csv

dict_ventes = {}
with open("ventes.json", "r", encoding="utf-8") as inventaire: # Référence: demo_json
    dict_ventes = json.load(inventaire)

dict_prix = {}
with open('prix.csv', 'r') as file: # Référence : demo_csv
    dict_reader = csv.DictReader(file) #Comme une liste de dictionnaires
    for row in dict_reader:
        dict_prix[row["Produit"]] = float(row["Prix"])

chiffre_affaire = 0
for key, value in dict_ventes.items():
    if key in dict_prix:
        tot_prix = dict_prix[key] * value
        chiffre_affaire += tot_prix

print("chiffre_affaire", chiffre_affaire)


