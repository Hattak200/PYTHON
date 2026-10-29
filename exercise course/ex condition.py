username = str(input("enter your username : "))
password = str(input("enter your password : "))
if username == "hamza" and password == "2009" :
    print("login successful")
elif username == "hamza"  or password == "2009" :
    print("the username or password was wrong")
else:
    print("login failed")
    
