from arquivos import carregar_dados, salvar_dados

ARQUIVO = "habitos.json"

def menu_habitos():
        print("=== Menu de Hábitos ===")
        print("1. Criar hábito")
        print("2. Ler todos os hábitos")
        print("3. Ler um hábito específico")
        print("4. Editar um hábito")
        print("5. Excluir um hábito")
        print("6. Sair")

def criar_habito():
    
    habitos = carregar_dados(ARQUIVO)
    
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

def main():
    while True:
        menu_habitos()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_habito()
        elif opcao == "2":
            ler_todos_habitos()
        elif opcao == "3":
            ler_um_habito()
        elif opcao == "4":
            editar_habito()
        elif opcao == "5":
            excluir_habito()
        elif opcao == "6":
            print("Saindo do menu de hábitos. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            
if __name__ == "__main__":    main()
