"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("> ")
    tokens = user_input.split(" ")
    
    if tokens[0] == "q":
        print("Thanks for using our calculator")
        break
    else:
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        if tokens[0] == "+":
            print(add(num1, num2))
            

# Replace this with your code
