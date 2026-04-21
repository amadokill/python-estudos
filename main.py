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


def Resposta():

    while True:
        op = input(Cores.cores["verde"] + "Escolha uma opção: " + Cores.cores["limpa"])
        if op == "1":
            print("Mostrando pessoas cadastradas...")
            break
        elif op == "2":
            print("Cadastrar nova pessoa...")
            break
        elif op == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


print(Msg("Cavalo".center(30)))
Resposta()
