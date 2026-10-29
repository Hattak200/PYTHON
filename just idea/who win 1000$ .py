print('''--------------WELCOM THE THE GAME ------------------: \n
█░█░█ █░█ █▀█   █░█░█ █ █░░ █░░   █░█░█ █ █▄░█   ▄█ █▀█ █▀█ █▀█  
▀▄▀▄▀ █▀█ █▄█   ▀▄▀▄▀ █ █▄▄ █▄▄   ▀▄▀▄▀ █ █░▀█   ░█ █▄█ █▄█ █▄█  🤑🤑🤑''')
print("Chaque bonne réponse vous rapporte 200 $. Au bout de 5 questions : 1000 $ !")
catégorie = str(input("Choisissez votre catégorie :  Culture générale  ,  Football : \n"))
prix = 0
if catégorie == "football" : 
    print("Vous sentez-vous capable de résister dans cette catégorie ?")
    Q1 = str(input("quelle est le buteur historique dans le coupe de monde avant le coupe du monde 2026 ? \n"))
    if Q1 == "klose" or  Q1 == "miroslav" or  Q1 == " miroslav klose" :
        print("congratulations ! tu as gagné le premier 200$")
        prix = prix + 200
        Q2 = str(input("quel pays a remporté la toute premiére coupe du monde en 1930 , \n"))
        if Q2 == "l'uruguay" or Q2 == "uruguay" :
            print("congratulations ! tu as gagné une autre 200$ , votre solde est 400$")
            prix = prix + 200
            Q3 = str(input("quel guardien est le seul de l'histoire à avoir remporté le ballon d'or ? , \n"))
            if Q3 == "lev" or  Q1 == "yachine" or  Q1 == " lev yachine" :
                print("congratulations ! tu as gagné une autre 200$ , votre solde est 600$")
                prix = prix + 200
                Q4 = str(input("donner le nom compléte d'un joueur qui a gagnée le ballon d'or et il a joue avec dortmund (2 joueur (aide)) ? , \n"))
                if Q4 == "ousmane dembélé" or Q2 == "matthias sammer" :
                     print("congratulations ! tu as gagné une autre 200$ , votre solde est 800$")
                     prix = prix + 200
                     Q5 = str(input("quel est le defenceur marocaine qui a joue avec juventus et bayern munchin et roma ? \n "))
                     if Q5 == "mehdi" or Q5 == "benatia" or Q5 == "mehdi benatia" :
                         print("congratulations ! tu as gagné le jeux , votre solde est 1000$")
                         prix = prix + 200
                     else :
                         print("mauvaise réponse ! tu as perdu")
                         
                else :
                    print("mauvaise réponse ! tu as perdu")   
            else :
                print("mauvaise réponse ! tu as perdu")           
        else :
             print("mauvaise réponse ! tu as perdu")
    else :
        print("mauvaise réponse ! tu as perdu")
if catégorie == "culture général" :
    print("Vous sentez-vous capable de résister dans cette catégorie ?")
    Q1 = str(input("quelle est le capital de espagne ? \n"))
    if Q1.lower() == "madrid"  :
            print("congratulations ! tu as gagné le premier 200$")
            prix = prix + 200
            Q2 = str(input("Quel est le plus grand océan du monde ? , \n"))
            if Q2.lower() == "pacifique"  :
                print("congratulations ! tu as gagné une autre 200$ , votre solde est 400$")
                prix = prix + 200
                Q3 = str(input("Quel est le symbole chimique de l’or ? , \n"))
                if Q3.lower() == "or"  :
                    print("congratulations ! tu as gagné une autre 200$ , votre solde est 600$")
                    prix = prix + 200
                    Q4 = str(input("Quel célèbre voyageur, né à Tanger en 1304, a parcouru une grande partie du monde connu ? , \n"))
                    if Q4.lower() == "ibn battouta"  :
                         print("congratulations ! tu as gagné une autre 200$ , votre solde est 800$")
                         prix = prix + 200
                         Q5 = str(input("Quel est l’élément chimique le plus abondant dans l’univers ? \n "))
                         if Q5.lower() == "l'hydrogéne"  :
                             print("congratulations ! tu as gagné le jeux , votre solde est 1000$")
                             prix = prix + 200
                         else :
                             print("mauvaise réponse ! tu as perdu")
                             
                    else :
                        print("mauvaise réponse ! tu as perdu")   
                else :
                    print("mauvaise réponse ! tu as perdu")           
            else :
                 print("mauvaise réponse ! tu as perdu")
    else :
            print("mauvaise réponse ! tu as perdu")
