import random 
n = int(input("enter the numbers of the club :  "))
list_club = []
list_point = []
league = {}
for i in range(0,n):
    club = input(f"enter name of the club {i+1} :  ") 
    list_club.append(club)
    s = 0
    for j in range(0,n-1):
        point = random.randint(0,3)
        if point != 2 :
            s = s + point
        else :
            continue
    list_point.append(s)
for i in range(0 , n):
    league[list_club[i]] = list_point[i]
max_pt = 0
min_pt = 10000
for v in league.values():
    if v >= max_pt :
        max_pt = v
    if v < min_pt :
        min_pt = v
for k , v in league.items():
    if v == max_pt :
        winner = k
    if v == min_pt :
        worst = k
print(f"the winner of the league is {winner} with {max_pt} point")
print(f"the worst club in the league is {worst} with {min_pt} point ")
valeurs = sorted(league.values() , reverse=True)
final_league = {}
for v in valeurs :
    for k in league :
        if league[k] == v :
           final_league[k] = v
print(final_league)
    


