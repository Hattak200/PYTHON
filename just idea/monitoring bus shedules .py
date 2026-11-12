#We have a route from the Abdelmalek Essaadi University area to the Mesnana and iberia and dradeb area, 
# served by several buses: 1-B, 2, and 21. The buses must arrive on time, 25 minutes in advance.
def analyze_reatrd(arrival_time):
    if arrival_time < 25:
        print("The bus is on time.")
    elif arrival_time == 25:
        print("The bus is arriving right on time.")
    else:
        print(f"The bus is late by {arrival_time - 25} minutes , and he is now in the area of {random_area()}.")
def random_area():
    import random
    areas = ["boukhalef", "maison de press", "akdital", "aswaq salam","ibn battouta"]
    return random.choice(areas)
print("Welcome to the Bus Schedule Monitoring System!")
print("Please enter the bus number you want to monitor (1-B, 2, or 21):")
bus_number = input()
if bus_number not in ["1-B", "2", "21"]:
    print("Invalid bus number. Please enter a valid bus number (1-B, 2, or 21).")  
elif bus_number == "1-B" :
    import random
    arrival_time = random.randint(0, 60)  # Simulate arrival time in minutes
    print(analyze_reatrd(arrival_time))
elif bus_number == "2" :
    import random
    arrival_time = random.randint(0, 60)  
    print(analyze_reatrd(arrival_time))
elif bus_number == "21" :
    import random
    arrival_time = random.randint(0, 60)  
    print(analyze_reatrd(arrival_time))



