from arquivos import carregar_dados, salvar_dados

ARQUIVO = "registros.json"
ARQUIVO_HABITOS = "habitos.json"
ARQUIVO_USUARIOS = "usuarios.json"

def criar_registro():

    registros = carregar_dados(ARQUIVO)
    habitos = carregar_dados(ARQUIVO_HABITOS)
    usuarios = carregar_dados(ARQUIVO_USUARIOS)

    while True:
        id_usuario = int(input("ID do Usuário: "))
        if id_usuario > 0:
            break
        print("Número inválido! O número deve ser maior que 0.")

    while True:
        id_habito = int(input("Habito ID: "))
        if id_habito > 0:
            break
        print("Número inválido! O número deve ser maior que 0.")
    while True:
        from datetime import datetime
        data = input("Data (dd/mm/aaaa): ")
        try:
            data_valida = datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida! Por favor, insira uma data válida.")
    while True:
        realizado = input("Realizado?(Sim/Não): ")
        if realizado in ["Sim", "Não", "sim", "não"]:
                break
        print("Opção inválida! Por favor dígite 'Sim' ou 'Não'.")

    

    registro = {
        "id": len(registros) + 1,
        "id_usuario": id_usuario,
        "id_habito": id_habito,
        "data": data,
        "realizado": realizado
    }

    registros.append(registro)
    salvar_dados(ARQUIVO, registros)
    print("Registro adicionado com sucesso!")

def listar_registros():

    registros = carregar_dados(ARQUIVO)

    if registros:
        for item in registros:
            print("ID de registro:", item["id"])
            print("Id do usuário:", item["id_usuario"])
            print("Id do hábito:", item["id_habito"])
            print("Data:", item["data"])
            print("Realizado:", item["realizado"])
            print()
    else:
        print("Nenhum registro encontrado.")

def atualizar_registro():

    registros = carregar_dados(ARQUIVO)


    while True:
        from datetime import datetime
        busca = (input("Digite o ID do registro que deseja atualizar:")).strip()
        try:
            busca = int(busca)
            if busca > 0:
                for item in registros:
                    if item ["id"] == busca:
                        while True:
                            item["data"] = input("Nova data (dd/mm/aaaa): ")
                            try:
                                datetime.strptime(item["data"], "%d/%m/%Y")
                                break
                            except ValueError:
                                print("Data inválida! Por favor, insira uma data válida.")
                        item["realizado"] = input("Realizado? (Sim/Não): ")
                        while item["realizado"] not in ["Sim", "Não", "sim", "não"]:
                            print("Opção inválida! Por favor dígite 'sim' ou 'Não'.")
                            item["realizado"] = input("Realizado? (Sim/Não): ")

                        print("Registro atualizado com sucesso!")
                        print()
                        salvar_dados()
                        return
                print("Nenhum registro encontrado.")
                return    
        except ValueError:
            print("O campo deve ser PREENCHIDO e deve conter apenas NÚMEROS.")
            return

def excluir_registro():

    registros = carregar_dados(ARQUIVO)


    while True:
        busca = (input("Digite o ID do registro que deseja excluir: ")).strip()
        try:
            busca = int(busca)
            if busca > 0:
                for item in registros:
                    if item["id"] == busca:
                        registros.remove(item)
                        print("Registro foi excluído com sucesso!")
                        print()
                        salvar_dados()
                        return
            print("Registro não encontrado.")
            return
        except ValueError:
            print("Você deve dígitar um valor.")

def procurar_registro():

    registros = carregar_dados(ARQUIVO)


    while True:
        busca = (input("Digite o ID do registro que deseja procurar: ")).strip()
        try:
            busca = int(busca)
            if busca > 0:
                for item in registros:
                    if item ["id"] == busca:
                        print("ID do usuario:", item["id_usuario"])
                        print("ID do hábito:", item["id_habito"])
                        print("Data:", item["data"])
                        print("Realizado:", item["realizado"])
                        print()
                        return
                print("Registro não encontrado.")
                return
        except ValueError:
            print("Dígite um valor.")
            
while True:
    print("-------Menu de registros-------")
    print()
    print("1 - Criar registro")
    print("2 - Listar registros")
    print("3 - Procurar registro")
    print("4 - Excluir registro")
    print("5 - Atualizar registro")
    print("0 - Sair")
    opcao = input("Escolha uma das opcões: ").strip()

    if opcao == "1":
        criar_registro()
    elif opcao == "2":
        listar_registros()
    elif opcao == "3":
      procurar_registro()
    elif opcao == "4":
        excluir_registro()
    elif opcao == "5":
        atualizar_registro()
    elif opcao == "0":
       print("Encerrando programa... Até logo!")
       break
    else:
        print("Opção inválida! Tente novamente.")