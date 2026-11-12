age = int(input("please enter your age : \n "))
license = bool(input("do you have a driving license ? (true or false) \n"))
if age >= 18 and license == True :
    print("you are allowed to drive")
elif age >= 18 and license == False :
    print("you are not allowed to drive")
else :
    print("you are not eligible to drive")