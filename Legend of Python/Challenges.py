# Write code below 💖
#Ask the user the month using input(). Check for the four seasons using an if/elif/eelse statement and logical operators: 1-3 are winter, 4-6 are Spring, 
#7-9 are Summer, 10-12 are Autumn. Everything else is invalid. Logical operators include and, and, or. Which to use. 

month = int(input("Enter the month number (1-12): "))
if month >= 1 and month <= 3:
    print("Winter 🌨️")
elif month >= 4 and month <= 6:
    print("Spring 🌱")
elif month >= 7 and month <= 9:
    print("Summer 🌻")
elif month >= 10 and month <= 12:
    print("Autumn 🍂")
else:
    print("Invalid")