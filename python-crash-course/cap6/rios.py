rios = {
    "rio amazonas": "brasil",
    "rio mississipi": "eua",
    "rio nilo": "egito",
}


for k, v in rios.items():
    print(f"O {k.title()}, corre no {v.title()}")

print("\nNomes dos rios: ")

for rio in rios.keys():
    print(rio.title())
print("\nNomes dos paises: ")
for pais in rios.values():
    print(pais.title())
