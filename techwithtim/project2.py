def calculator():
    try:
        print("Welcome to the calculator!")
        a = int(input("Enter a number One: "))

        operator = input("Enter an operator: ")

        b = int(input("Enter a number Two: "))

#switch case
        match operator:
          case "+":
           print("The result is: ", a + b)
          case "-":
           print("The result is: ", a - b)
          case "*":
           print("The result is: ", a * b)
          case "/":
           print("The result is: ", a / b)
          case _:
            print(f"Invalid operator {operator}")
    except ValueError:
      print("Invalid input. Please enter numbers only.")
calculator()   
    