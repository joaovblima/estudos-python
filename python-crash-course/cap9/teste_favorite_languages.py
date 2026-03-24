from collections import OrderedDict

linguagens_favoritas = OrderedDict()

linguagens_favoritas["joao"] = "python"
linguagens_favoritas["ingrid"] = "clojure"
linguagens_favoritas["maria sofia"] = "javascript"
linguagens_favoritas["maria alice"] = "java"

for nome, linguagem in linguagens_favoritas.items():
    print(nome.title(), "->", linguagem.title())
