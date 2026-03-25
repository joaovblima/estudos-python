arquivo = input("qual o nome do seu arquivo? ")

with open(arquivo) as f_o:
    for line in f_o:
        print(line.strip())
