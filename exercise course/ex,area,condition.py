area = str(input("choose an area : tanger , casa , rabat , fes : \n"))
if area.lower() == "tanger" :
    print(f"you are in {area} , the weather is sunny")
elif area.upper() == "CASA" :
    print(f"you are in {area} , the weather is rainy")
elif area.lower() == "rabat" :
    print(f"you are in {area} , the weather is cloudy")
elif area.upper() == "FES" :
    print(f"you are in {area} , the weather is snowy")
else :
    print("the area you entered is not in the list of available areas")