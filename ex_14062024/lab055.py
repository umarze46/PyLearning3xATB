num = float(input("Enter a number: "))

match num:
    case 1:
        print("You've entered a valid number")
        print("Thank you")
    case _:
        print("You've entered an invalid number")
        print("Try again")
