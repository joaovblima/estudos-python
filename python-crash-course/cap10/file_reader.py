# utilizo uma variável para passar o caminho do arquivo(tem que esta no mesmo diretorio)
#
arquivo = "avemaria.txt"
# com a funcao with e a funcao open eu "abro" o arquivo passando o caminho delee
# a variavel file_objetct representa meu arquivo

with open(arquivo) as file_object:
    for line in file_object:
        print(line)
    # a variavel conteudo representa como o nome ja diz, o conteudo do meu arquivo
    # ai eu passo a variavel file_object em seguida de read, para evidentemente ler meu arquivo
    # depois eu dou print em conteudo, que armazena tudo que tem no arquivo
    # conteudo = file_object.read()
    # print(conteudo)
    #
