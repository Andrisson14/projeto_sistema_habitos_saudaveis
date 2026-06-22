from arquivos import carregar_dados, salvar_dados


ARQUIVO = "usuarios.json"


def ler_nome():
    while True:
        nome = input("Nome: ").strip()
        if nome != "":
            return nome
        print("Erro: o nome não pode ficar vazio.")

def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("Erro: digite um número maior que zero.")
        except ValueError:
            print("Erro: digite apenas números inteiros.")

def ler_float_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print("Erro: digite um número maior que zero.")
        except ValueError:
            print("Erro: digite apenas números válidos.")

def cadastrar_usuario():

    usuarios = carregar_dados(ARQUIVO)

    id_usuario = max((u["id"] for u in usuarios), default=0) + 1

    nome = ler_nome()
    idade = ler_inteiro_positivo("Idade: ")
    peso = ler_float_positivo("Peso: ")
    altura = ler_float_positivo("Altura: ")


    usuario = {
        "id": id_usuario,
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura
    }
    usuarios.append(usuario)
    salvar_dados(ARQUIVO, usuarios)


    print("\nUsuário cadastrado com sucesso!")
    print(f"ID do usuário: {id_usuario}")

def listar_usuarios():

    usuarios = carregar_dados(ARQUIVO)

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return


    for usuario in usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Peso: {usuario['peso']} kg")
        print(f"Altura: {usuario['altura']} m")
        print("-" * 30)

def buscar_usuario():

    usuarios = carregar_dados(ARQUIVO)

    id_busca = ler_inteiro_positivo("Digite o ID do usuário: ")


    for usuario in usuarios:
        if usuario["id"] == id_busca:
            print(f"\nID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Peso: {usuario['peso']} kg")
            print(f"Altura: {usuario['altura']} m")
            return


    print("Usuário não encontrado.")

def atualizar_usuario():

    usuarios = carregar_dados(ARQUIVO)

    id_busca = ler_inteiro_positivo(
        "Digite o ID do usuário que deseja atualizar: "
    )


    for usuario in usuarios:
        if usuario["id"] == id_busca:
            usuario["nome"] = ler_nome()
            usuario["idade"] = ler_inteiro_positivo("Nova idade: ")
            usuario["peso"] = ler_float_positivo("Novo peso: ")
            usuario["altura"] = ler_float_positivo("Nova altura: ")


            salvar_dados(ARQUIVO, usuarios)
            print("Usuário atualizado com sucesso!")
            return


    print("Usuário não encontrado.")

def excluir_usuario():

    usuarios = carregar_dados(ARQUIVO)

    id_busca = ler_inteiro_positivo(
        "Digite o ID do usuário que deseja excluir: "
    )


    for usuario in usuarios:
        if usuario["id"] == id_busca:
            usuarios.remove(usuario)
            salvar_dados(ARQUIVO, usuarios)
            print("Usuário excluído com sucesso!")
            return


    print("Usuário não encontrado.")
