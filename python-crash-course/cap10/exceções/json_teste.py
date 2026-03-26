import json

numeros = [2, 3, 5, 7, 11, 13]

arquivo = "numeros.json"

with open(arquivo, "w") as f_obj:
    json.dump(numeros, f_obj)
