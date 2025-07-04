print("Welcom to the random color generator ! Let's get started")

def random_color():
     while True:
         enter_button = input("Press enter to continue: ")
         if(enter_button == ""):
          colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
          for color in colors:
           print(color)
           print("These are the colors available! Eveytime you enter a color, it will be randomly generated")
         else:
            print("You have entered the wrong button ! Please try again")
            break

random_color()
