from arquivos import carregar_dados, salvar_dados

ARQUIVO = "habitos.json"
ARQUIVO_USUARIOS = "usuarios.json"


def criar_habito():
    
    habitos = carregar_dados(ARQUIVO)
    usuarios = carregar_dados(ARQUIVO_USUARIOS)

    while True:
        id_usuario = input("ID do Usuário: ").strip()
        try:
            id_usuario = int(id_usuario)
        except ValueError:
            print("Você deve digitar um número.")
            continue
        if id_usuario <= 0:
            print("Número inválido! O número deve ser maior que 0.")
            continue
        if not any(u["id"] == id_usuario for u in usuarios):
            print("Usuário não encontrado! Digite um ID de usuário existente.")
            continue
        break
    
    while True:
        nome = input("Informe um hábito (ex: Beber água, Caminhada): ").strip()
        if nome:
            break
        print("O nome do hábito não pode ficar vazio. Tente novamente.")

    categorias_validas = ["alimentação", "sono", "atividade física", "outro"]
    while True:
        categoria = input("Categoria (alimentação / sono / atividade física / outro): ").strip().lower()
        if categoria in categorias_validas:
            break
        print(f"Categoria inválida. Escolha entre: {', '.join(categorias_validas)}.")

    while True:
        meta_diaria = input("Meta diária (ex: 8 copos, 30 minutos): ").strip()
        if meta_diaria:
            break
        print("A meta diária não pode ficar vazia. Tente novamente.")

   
    novo_id = max((h["id"] for h in habitos), default=0) + 1

    habito = {
        "id": novo_id,
        "id_usuario": id_usuario,
        "nome": nome,
        "categoria": categoria,
        "meta_diaria": meta_diaria
    }

    habitos.append(habito)
    salvar_dados(ARQUIVO, habitos)
    print(f"Hábito '{nome}' cadastrado com sucesso!")


def ler_todos_habitos():
    habitos = carregar_dados(ARQUIVO)

    if not habitos:
        print("Nenhum hábito cadastrado.")
        return
    
    print("Lista de Hábitos Cadastrados:")
    print("-" * 20)
    for h in habitos:
        print(f"ID: {h['id']}")
        print(f"ID do Usuário: {h['id_usuario']}")
        print(f"Nome: {h['nome']}")
        print(f"Categoria: {h['categoria']}")
        print(f"Meta diária: {h['meta_diaria']}")
        print("-" * 20)
    print()

def ler_um_habito():
    
    habitos = carregar_dados(ARQUIVO)
    
    if not habitos:
        print("Nenhum hábito cadastrado.")
        return

    while True:
        entrada = input("Digite o ID do hábito: ").strip()
        try:
            id_habito = int(entrada)
            if id_habito <= 0:
                print("O ID deve ser um número positivo. Tente novamente.")
                continue
            break
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")

    for h in habitos:
        if h["id"] == id_habito:
            print("Detalhes do Hábito:")
            print(f"ID: {h['id']}")
            print(f"ID do Usuário: {h['id_usuario']}")
            print(f"Nome: {h['nome']}")
            print(f"Categoria: {h['categoria']}")
            print(f"Meta diária: {h['meta_diaria']}")
            return

    print("Hábito não encontrado.")

def editar_habito():
    habitos = carregar_dados(ARQUIVO)

    if not habitos:
        print("Nenhum hábito cadastrado.")
        return
    while True:
        try:
            id_habito = int(input("Digite o ID do hábito que deseja editar: "))
            for h in habitos:
                if h["id"] == id_habito:
                    print("Informe os novos dados (deixe em branco para manter o valor atual):")
                    novo_nome = input(f"Nome atual ({h['nome']}): ")
                    nova_categoria = input(f"Categoria atual ({h['categoria']}): ")
                    nova_meta_diaria = input(f"Meta diária atual ({h['meta_diaria']}): ")

                    if novo_nome:
                        h["nome"] = novo_nome
                    if nova_categoria:
                        h["categoria"] = nova_categoria
                    if nova_meta_diaria:
                        h["meta_diaria"] = nova_meta_diaria

                    salvar_dados(ARQUIVO, habitos)
                    print("Hábito atualizado com sucesso!")
                    return
            print("Hábito não encontrado.")
        except ValueError:
            print("ID inválido. Por favor, digite um ID válido.")
            

def excluir_habito():
    habitos = carregar_dados(ARQUIVO)

    if not habitos:
        print("Nenhum hábito cadastrado.")
        return

    try:
        id_habito = int(input("Digite o ID do hábito que deseja excluir: "))
        for h in habitos:
            if h["id"] == id_habito:
                habitos.remove(h)
                salvar_dados(ARQUIVO, habitos)
                print("Hábito excluído com sucesso!")
                return
        print("Hábito não encontrado.")
    except ValueError:
        print("ID inválido. Por favor, digite um ID válido.")


