usuarios_atuais = ["joao", "ingrid", "maria alice", "maria sofia"]
novos_usuarios = ["lidiane", "cicera", "ingrid", "maria sofia"]

for usuario in novos_usuarios:
    if usuario in usuarios_atuais:
        print("Por favor, escolha outro nome, esse esta sendo usado")
    else:
        print("Nome do usuario esta disponivel")
