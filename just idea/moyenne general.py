# chaque matiere un examen et coefficient : 
# mathématiques : coefficient 7 – 3 examen
#Physique-Chimie : coefficient 7 – 3 examen 
#SVT (Sciences de la Vie et de la Terre) : coefficient 5  – 3 examen 
#Philosophie : coefficient 2 – 2 examen 
#Anglais : coefficient 2 – 2 examen 
#Français : coefficient 4 – 2 examen 
#Arabe : coefficient 2 – 2 examen 
math = []
for i in range(3):
    while note < 0 or note > 20 :
        print("La note doit être entre 0 et 20.")
    note = float(input("Entrez la note de l'examen de mathématiques {}: ".format(i + 1)))
    math.append(note)
physique = []
for i in range(3):
    while note < 0 or note > 20 :
        print("La note doit être entre 0 et 20.")
    note = float(input(f"entrez la note de l'examen physique-chimie {i+1} : "))
    physique.append(note)
svt = []
for i in range(3) :
    while note < 0 or note > 20 :
        print("La note doit être entre 0 et 20.")
    note = float(input(f"entrez la note de l'examen svt {i+1} :"))
    svt.append(note)
philosophie = []
for i in range(2):
    while note < 0 or note > 20 :
        print("La note doit être entre 0 et 20.")
    note = float(input(f"entrez la note de l'examen philosophie {i+1} :"))
    philosophie.append(note)
anglais = []
for i in range(2):
    while note < 0 or note > 20 :
        print("La note doit être entre 0 et 20.")
    note = float(input(f"entrez la note de l'examen anglais {i+1} :"))
    anglais.append(note) 
francais = []
for i in range(2):
    while note < 0 or note > 20 :
        print("La note doit être entre 0 et 20.")
    note = float(input(f"entrez la note de l'examen francais {i+1} :"))
    francais.append(note)
arabe = []
for i in range(2):
    while note < 0 or note > 20 :
        print("La note doit être entre 0 et 20.")
    note = float(input(f"entrez la note de l'examen arabe {i+1} :"))
    arabe.append(note)
moy = (sum(math) * 7 + sum(physique) * 7 + sum(svt) * 5 + sum(philosophie) * 2 + sum(anglais) * 2 + sum(francais) * 4 + sum(arabe) * 2) / (7*3 + 7*3 + 5*3 + 2*2 + 2*2 + 4*2 + 2*2)
if moy <10 :
    print(f"malheureusement, vous êtes recalé. Votre moyenne est : {moy}")
elif moy < 12 and moy >= 10:
    print(f" vous êtes admis. Votre moyenne est : {moy}")
elif moy < 14 and moy >= 12:
    print(f"  assez bien , votre moyenne est : {moy}")
elif moy < 18 and moy >= 14:
    print(f"Bien, votre moyenne est : {moy}")
else:
    print(f"Félicitations ! Votre note est : {moy} Très bien")
 