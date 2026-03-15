def formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name


while True:
    print("Please tell me your name? ")
    print("Enter 'q' at any time quit")
    f_name = input()
    if f_name == 'q':
        break
    print("Your last name? ")
    l_name = input()
    if l_name == 'q':
        break
    ftd_name = formatted_name(f_name, l_name)
    print("Hello ", ftd_name.title())
