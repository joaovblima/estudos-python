usuarios_nao_confirmados = ["alice", "brian", "candace"]
usuarios_confirmados = []

while usuarios_nao_confirmados:
    usuario_atual = usuarios_nao_confirmados.pop()
    print("Verificando usuario", usuario_atual.title())
    usuarios_confirmados.append(usuario_atual)

print("Os usuarios seguintes estao confirmados: ")
for usuario in usuarios_confirmados:
    print(usuario.title())
