import json

bulletin = {}
lst_noms = []

while True:
    lst_matiere = []
    lst_notes = [[]]
    dict_notes = {}
    nom = input("Entrez le nom de l'étudiant : ")
    if nom != "":
        lst_noms.append(nom)
        index_note = 0
        while True:
            matiere = input("Entrez la matière : ")
            if matiere != "":
                lst_matiere.append(matiere)
                notes = []
                while True:
                    note = input("Entrez la note : ")
                    if note != "":
                        notes.append(int(note))
                    else:
                        lst_notes.append(notes)
                        index_note += 1
                        break
            else:
                break
        for i in range(len(lst_matiere)):
            dict_notes.update({lst_matiere[i]:lst_notes[i]})
        note_etu = {nom:dict_notes}
        bulletin.update(note_etu)
    else:
        break

with open("bulletin_notes.json", "w", encoding="utf-8") as f:
    json.dump(bulletin, f, ensure_ascii=False, indent=4)               #https://docs.python.org/3/library/json.html