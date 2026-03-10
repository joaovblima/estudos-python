usuarios = ["joao", "ingrid", "maria alice",
            "maria sofia", "admin"]
# usuarios = []
if not usuarios:
    print("nao ha usuarios na lista")
    print("precisamos achar alguns usuarios")
else:
    for usuario in usuarios:
        if usuario == "admin":
            print("Ola", usuario.title(), "gostaria de ver relatorio de status?")
        else:
            print("Ola", usuario.title(), "obrigado por fazer login novamente")
