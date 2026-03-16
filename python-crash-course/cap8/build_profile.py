def build_profile(first, last, **user_info):
    """
        Funcao que cria um 'perfil de usuario' de acordo 
        com as informacoes passadas pelo usuario evidentemente. 
        '**user_info' quer dizer que posso passar a quantidade arbitraria 
        de informacoes que posteriormente serao armazenadas no meu dicionario de informacoes, 
        as condicoes de uso eh que tenho que passar uma chave e um valor, exemplo:
        casado="sim", prossiao="desenvolvedor de software" quer dizer que posso passar a quantidade arbitraria 
        de informacoes que posteriormente serao armazenadas no meu dicionario de informacoes, 
        as condicoes de uso eh que tenho que passar uma chave e um valor, exemplo:
        casado="sim", prossiao="desenvolvedor de software".
    """
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last

    for k, v in user_info.items():
        profile[k] = v

    return profile


joao = build_profile("joao", "lima", location="uniao dos palmares",
                     hobby="jiujitsu", fav_team="barcelona")
joao_lima = build_profile("joao", "lima", religiao="catolico", comida_favorita="file a parmegiana",
                          time_do_coracao="spfc", livro_preferido="confissoes")

print(joao)
print(joao_lima)
