import json


def json_csv(fichier1,fichier2):
    with open(str(fichier1) + ".json") as etudiant:
        etudiant = json.load(etudiant)


    fichier = open(str(fichier2) +".txt","w")
    for student in etudiant:
        for key,value in student.items():
            fichier.write(str(key) + ": " +str(value) + "\n")
        fichier.write("\n\n")
    fichier.close()
    


