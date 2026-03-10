#Create a weight conversion program that asks the user for their Earth weight as a float, asks the user for a plan number as an int. Use an if/elif/else to calculate
#the user's weight on the destination planet. 
#Destination weight = Earth weight x Realtive gravity of destination planet. 
#Planets: 1. Mercury (0.38), 2. Venus (0.91), 3. Mars (0.38), 4. Jupiter (2.53), 5. Saturn (1.07), 6. Uranus (0.89), 7. Neptune (1.14)
#If a user enters a planet number that is not 1-7, print "Invalid number".

Weight = float(input("Enter your Earth weight: "))
Planet = int(input("Enter the planet number (1-7): "))  
if Planet == 1:
    Destination_weight = Weight * 0.38
    print(f"Your weight on Mercury is: {Destination_weight:.2f}")   
elif Planet == 2:
    Destination_weight = Weight * 0.91
    print(f"Your weight on Venus is: {Destination_weight:.2f}")   
elif Planet == 3:
    Destination_weight = Weight * 0.38
    print(f"Your weight on Mars is: {Destination_weight:.2f}")   
elif Planet == 4:
    Destination_weight = Weight * 2.53
    print(f"Your weight on Jupiter is: {Destination_weight:.2f}")   
elif Planet == 5:
    Destination_weight = Weight * 1.07
    print(f"Your weight on Saturn is: {Destination_weight:.2f}")   
elif Planet == 6:
    Destination_weight = Weight * 0.89
    print(f"Your weight on Uranus is: {Destination_weight:.2f}")   
elif Planet == 7:
    Destination_weight = Weight * 1.14
    print(f"Your weight on Neptune is: {Destination_weight:.2f}")   
else:
    print("Invalid number")