from arquivos import carregar_dados, salvar_dados

ARQUIVO = "habitos.json"

def criar_habito():
    habitos = carregar_dados(ARQUIVO)

    nome = input("informe um hábito (ex: Beber água, Caminhada): ")
    categoria = input("Categoria (alimentação / sono / atividade física / outro): ")
    meta_diaria = input("Meta diária (ex: 8 copos, 30 minutos): ")

    habito = {
        "id": len(habitos) + 1,
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

    print("Lista de Hábitos:")
    for h in habitos:
        print("Lista de Hábitos Cadastrados:")
    for h in habitos:
        print(f"ID: {h['id']}")
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
    
    try:
        id_habito = int(input("Digite o ID do hábito: "))
        for h in habitos:
            if h["id"] == id_habito:
                print("Detalhes do Hábito:")
                print(f"Nome: {h['nome']}")
                print(f"Categoria: {h['categoria']}")
                print(f"Meta diária: {h['meta_diaria']}")
                return
        print("Hábito não encontrado.")
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
