import json

arquivo = "numeros.json"

with open(arquivo) as f_obj:
    numeros = json.load(f_obj)
    print(numeros)
