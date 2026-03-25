arquivo = "digitos.txt"

with open(arquivo) as file_object:
    lines = file_object.readlines()
    digitos_string = ""
    for line in lines:
        digitos_string += line.rstrip()

    print(digitos_string)
    print(len(digitos_string))
