from arquivos import carregar_dados


ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_HABITOS = "habitos.json"


def relatorio_geral():

    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    habitos = carregar_dados(ARQUIVO_HABITOS)

    print("\n===== RELATÓRIO GERAL =====")

    print(f"Quantidade de usuários: {len(usuarios)}")
    print(f"Quantidade de hábitos cadastrados: {len(habitos)}")

    print("\nHábitos por categoria:")

    categorias = {}

    for habito in habitos:
        categoria = habito["categoria"]

        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1


    for categoria, quantidade in categorias.items():
        print(f"- {categoria}: {quantidade}")


def relatorio_usuario():

    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    habitos = carregar_dados(ARQUIVO_HABITOS)


    id_usuario = int(input("\nDigite o ID do usuário: "))


    usuario_encontrado = None


    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario_encontrado = usuario


    if usuario_encontrado is None:
        print("Usuário não encontrado.")
        return


    print("\n===== RELATÓRIO DO USUÁRIO =====")

    print(f"Nome: {usuario_encontrado['nome']}")
    print(f"Idade: {usuario_encontrado['idade']}")
    print(f"Peso: {usuario_encontrado['peso']} kg")
    print(f"Altura: {usuario_encontrado['altura']} m")


    print("\nHábitos cadastrados:")


    encontrou = False


    for habito in habitos:

        if habito["id_usuario"] == id_usuario:

            encontrou = True

            print("----------------")
            print(f"Hábito: {habito['nome']}")
            print(f"Categoria: {habito['categoria']}")
            print(f"Meta diária: {habito['meta_diaria']}")


    if encontrou == False:
        print("Nenhum hábito cadastrado.")


def menu_relatorios():

    while True:

        print("\n===== RELATÓRIOS =====")
        print("1 - Relatório geral")
        print("2 - Relatório por usuário")
        print("0 - Voltar")


        opcao = input("Escolha: ")


        if opcao == "1":
            relatorio_geral()


        elif opcao == "2":
            relatorio_usuario()


        elif opcao == "0":
            break


        else:
            print("Opção inválida.")