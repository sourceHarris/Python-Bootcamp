def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mul(n1, n2):
    return n1 * n2

# dictionary = {
#     "+": add,
#     "-": sub,
#     "/": div,
#     "*": mul,
# }
#
# print(dictionary["*"](4,8))
#



def checker(value, n1, n2):

    if value == "+":
        output = add(n1, n2)
        return output

    elif value == "-":
        output = sub(n1, n2)
        return output

    elif value == "*":
        output = mul(n1, n2)
        return output

    elif value == "/":
        output = div(n1, n2)
        return output

    return f"{value} undefined {value} = 0.0"

def calculator():
    game_not_over = True
    first_num = float(input("What's the first number: "))
    while game_not_over:

        choices = "+\n-\n*\n/\n"
        print(choices)
        operation = input("Pick an operation: ")
        second_num = float(input("What's the second number: "))

        answer = checker(value=operation, n1=first_num, n2=second_num)
        print(f"{first_num} {operation} {second_num} = {answer}")

        ask = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")

        if ask == "y":
            first_num = answer
        else:
            print("\n" * 20)
            calculator()



calculator()
