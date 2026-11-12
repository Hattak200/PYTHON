notes = { "math" : 18 , "pc" : 20 , "informatique" : 19}
s = 0 
for i in notes:
    s = s + notes[i]
print("la somme est : " , s)








etudiant = { "nom" : "dupont" , "age" : 21 , "ville" : 'paris' }
print("les informations de l'etudiant sont : " , etudiant ["nom"] , etudiant["age"])
etudiant["matiere"] = "informatique"
etudiant["ville"]  = "lyon"
print("les informations de l'etudiant sont : " , etudiant)

