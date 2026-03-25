arquivo = "dog.txt"

with open(arquivo) as file_object:
    lines = file_object.read()
    print(lines.replace("dog", "cat"))
teste = "dog dog dog dog, dog dog dog dog"
print(teste.replace("dog", "cat"))
print(teste)
