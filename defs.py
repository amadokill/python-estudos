import Cores


def Msg(msg):
    c = Cores.cores
    r = len(msg)
    print(Cores.cores["azul"] + "-" * r)
    print(Cores.cores["verde"] + msg)
    print(Cores.cores["azul"] + "-" * r)

    return (
        f"{c['amarelo']}1{c['limpa']} - {c['roxo']}Ver Pessoas Cadastradas{c['limpa']}\n"
        f"{c['amarelo']}2{c['limpa']} - {c['roxo']}Cadastrar nova pessoa{c['limpa']}\n"
        f"{c['amarelo']}3{c['limpa']} - {c['roxo']}Sair{c['limpa']}"
    )


def Resposta(nome):

    while True:
        op = input(Cores.cores["verde"] + "Escolha uma opção: " + Cores.cores["limpa"])
        if op == "1":
            print("Mostrando pessoas cadastradas...")
            LerArquivo(nome)

        elif op == "2":
            print("Cadastrar nova pessoa...")
            nom = input("Digite o nome a ser adcionado: ")
            idade = int(input("Digite a indade a ser adcionada: "))
            Cadastro(nome, nom, idade)

        elif op == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


def CriarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close
    except:
        print(Cores.cores["vermelho"] + "Erro" + Cores.cores["limpa"])
    else:
        print(Cores.cores["verde"] + "Criado com sucesso" + Cores.cores["limpa"])


def LerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro")
    else:
        print(a.read())


def ArquivoExiste(nome):
    try:
        a = open(nome, "rt")
    except FileNotFoundError:
        CriarArquivo(nome)
    else:
        True


def Cadastro(arq="", nom="", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um erro ao executar o arquivo")
    else:
        try:
            a.write(f"Nome: {nom}|Idade: {idade}\n")
        except:
            print("Houve um erra ao tentar escrever no arquivo")
