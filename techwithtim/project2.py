a = int(input("Enter a number One: "))

operator = input("Enter an operator: ")

b = int(input("Enter a number Two: "))

#switch case
match operator:
    case "+":
      print(a + b)
    case "-":
      print(a - b)
    case "*":
      print(a * b)
    case "/":
     print(a / b)
    case _:
      print(f"Invalid operator {operator}")
   
    