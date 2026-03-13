pedidos_de_sanduiche = ["x-bestafera", "x-file", "pastrami", "zumbi dos palmares",
                        "armlock", "baunilha fofinho", "pastrami", "pastrami"]
pedidos_finalizados = []

if "pastrami" in pedidos_finalizados:
    print("estamos sem pastrami disponivel")
while pedidos_de_sanduiche:
    # removo sanduiche para adicionar na lista de pedidos_finalizados
    sanduiche = pedidos_de_sanduiche.pop()
    # checo se existe foi solicitado sanduiche de pastrami
    # utilizo continue para pular o pastrami
    if sanduiche == "pastrami":
        continue
    print("Preparei seu", sanduiche)
    pedidos_finalizados.append(sanduiche)

print("\nPedidos de sanduiches finalizados: ")
for sanduiche in pedidos_finalizados:
    print(sanduiche.title())
