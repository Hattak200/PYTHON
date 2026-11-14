print('''you have a robot that moves on a coordinate plane , the robot starts at the origin : (x,y) = (0,0) 
 four commands you can be executed :
                                    RIGHT = +1
                                    left  = -1
                                    up    = +1
                                    down  = -1
you can enter just r , l , u , d  with space between the commands''')
def robot_distance(x,y) :
   return abs(x) + abs(y)
commands = input("enter your commands :  ")
list = commands.split()
x = 0
y = 0
for i in range(0 , len(list)) :
     if list[i].lower() == "r" :
        x += 1
     elif list[i].lower() == "l":
        x -= 1
     elif list[i].lower() == "u":
        y += 1
     elif list[i].lower() == "d":
        y -= 1
     else :
        continue
print(f"the distance between his final position and the starting point is : {robot_distance(x,y)}")
        




