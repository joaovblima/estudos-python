def fazer_sanduiches(*ingredientes):
    print("\nSeu sanduiche vai ser feito com:")
    for ingrediente in ingredientes:
        print("-" + ingrediente)


fazer_sanduiches("bacon", "file", "queijo", "salada")
fazer_sanduiches("ovo", "hamburguer", "salsicha")
fazer_sanduiches("queijo", "presunto")
