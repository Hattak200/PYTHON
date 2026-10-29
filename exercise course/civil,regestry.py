natio = str(input("are you morrocan ? (yes or no) \n"))
if natio.lower() == "yes" :
    age = int(input("please enter your age :  "))
    if age >= 18 :
        print("you are allowed to create a card")
    else :
        print("you are not allowed to create a card")
elif natio.lower() == "no" :
    print("you are not allowed to create a card")