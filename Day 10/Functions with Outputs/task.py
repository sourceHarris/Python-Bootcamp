def format_name(f_name, l_name):
    first_name = f_name
    last_name = l_name

    return f"Your name is {first_name.title()} {last_name.title()}!"

name1 = input("What is your first name: ")
name2 = input("What is your last name: ")

our_function =format_name(f_name=name1, l_name=name2)

print(our_function)