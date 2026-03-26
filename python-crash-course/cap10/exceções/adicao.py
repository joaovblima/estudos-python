"""
continuar = True

while continuar:
    num_1 = int(input("digite um numero? "))
    num_2 = int(input("digite outro numero? "))
    try:
        soma = num_1 + num_2
        print(f"a soma de {str(num_1)} + {str(num_2)} é: {str(soma)}")
    except ValueError:
        print("Por favor, digite um número.")

    opcao = input("Deseja continuar? (s/n)")
    if opcao == "n":
        continuar = False
"""

num_1 = input("digite um numero? ")
num_2 = input("digite outro numero? ")
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    soma = num_1 + num_2
    print("o valor da soma é: " + str(soma))

except ValueError:
    print("Você deve digitar um número válido")
