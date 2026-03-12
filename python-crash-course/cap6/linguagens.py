linguagens_favoritas = {
    "joao": "python",
    "matheus": "c++",
    "ingrid": "lua",
    "leticia": "elixir",
    "maria sofia": "clojure",
    "maria alice": "kotlin",
}
"""
print("A linguagem favorita de Maria Sofia eh " +
      linguagens_favoritas["maria sofia"].title())

for nome in linguagens_favoritas.keys():
    print(nome.title())

melhores_amigos = ["ingrid", "maria sofia"]
for nome in linguagens_favoritas.keys():
    print(nome.title())
    if nome in melhores_amigos:
        print(f"Ola {nome.title()}, vi que sua linguagem favorita eh {
              linguagens_favoritas[nome].title()}")

if "erin" not in linguagens_favoritas.keys():
    print("eita chefe Erin, participou nem da pesquisa")

for nome in sorted(linguagens_favoritas.keys()):
    print(nome.title() + ", obrigado por responder a pesquisa.")
print("as seguintes linguagens foram mencionadas: ")
for linguagem in linguagens_favoritas.values():
    print(linguagem)

"""
novas_pessoas_entrevistadas = ["cicera", "iris", "maria alice", "vitoria"]

for nome in novas_pessoas_entrevistadas:
    if nome in linguagens_favoritas.keys():
        print("Nao precisa participar novamente da enquente", nome.title(),
              "fique de boa pai")
    else:
        print("Fique a vontade para responder a pergunta", nome.title())
