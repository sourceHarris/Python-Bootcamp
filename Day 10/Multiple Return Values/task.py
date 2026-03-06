# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100==0:

            if year % 400 == 0:
                return "Leap"
            else:
                return "Not Leap"

        else:
            return "Not Leap"
    else:
        return "Not Leap"

print(is_leap_year(int(input("Enter the year: "))))