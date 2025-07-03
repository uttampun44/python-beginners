name = input("Enter your name: ").lower()

print("Hello " + name)

should_we_drinnk = input("Should we drink? (yes/no): ")

drinks = ["water", "juice", "soda", "beer", "wine"]

if(should_we_drinnk == "yes" or should_we_drinnk == "y"):
    print("Select a drink from the list:")

    for drink in drinks:
        print(drink)

    selected_drink = input("Enter the drink you want: ").lower()
    
    if selected_drink in drinks:
        print("Drinking " + selected_drink + " now!")
        print("Enjoy your drink, " + name + "!")
    else:
        print("Sorry, we don't have that drink.")
        
else:
    print("Let's not drink then.")