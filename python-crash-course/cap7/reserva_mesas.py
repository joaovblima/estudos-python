quantidade_pessoas = int(input("Voces estao em quantas pessoas? "))
if quantidade_pessoas > 8:
    print(f"Nao temos mesas para {
          str(quantidade_pessoas)} pessoas, por favor aguarde.")
else:
    print("Ok senhor, sua mesa esta pronta.")
