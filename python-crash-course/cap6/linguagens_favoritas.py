linguagens_favoritas = {
    "joao": ["python", "clojure"],
    "matheus": ["c"],
    "lidiane": ["java", "kotlin"],
    "ana leticia": ["rust", "c++"],
}

for nome, linguagens in linguagens_favoritas.items():
    print("A linguagem favorita de", nome, ":")
    for linguagem in linguagens:
        print(linguagem)
