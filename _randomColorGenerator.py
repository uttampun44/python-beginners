import random

print("Welcom to the random color generator ! Let's get started")

def random_color():
     colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
     shuffle_colors = colors[:]
     random.shuffle(shuffle_colors)
    
     while True:
         enter_button = input("Press enter to continue or n to exit: ")
         if(enter_button.lower() == "n"):
             print("You exited the program")
             break
         elif(enter_button == ""):
            print("These are the colors available! Eveytime you enter a color, it will be shuffled")
            print(shuffle_colors)

            color = input("Enter a color: ")
            if(color in shuffle_colors):
                print(f"You have selected a valid color! The color is: {color}")
                print(color)
            else:
                print("The color is not available")
         else:
            print("The color you entered is not available")
random_color()
