registros = []

def criar_registro():

    id_usuario = int(input("ID do Usuário: "))
    id_habito = int(input("Habito ID: "))
    data = input('Data (dd/mm/aaaa): ')
    realizado = input("Realizado?(Sim/Não): ")

    registro = {
     "id": len(registros)+ 1,
     "id_usuario": id_usuario,  
     "id_habito": id_habito,
     "data": data,
     "realizado": realizado
    }

    registros.append(registro)
    print("Registro adicionado com sucesso!")

def listar_registros():
    if registros:
        for item in registros:
            print("Id do usuário:", item["id_usuario"])
            print("Id do hábito:", item["id_habito"])
            print("Data:", item["data"])
            print("Realizado:", item["realizado"])
    else:
        print("Nenhum registro encontrado.")

def atualizar_registro():
    busca = int(input("Digite o ID do registro que deseja atualizar:"))
    for item in registros:
        if item ["id"] == busca:
            item["id_usuario"] = input("Novo ID do usuário: ")
            item["id_habito"] = input("Novo ID do hábito: ")
            item["data"] = input("Nova data (dd/mm/aaaa): ")
            item["realizado"] = input("Realizado? (Sim/Não): ")
            print("Registro atualizado com sucesso!")
            return

def excluir_registro():
    busca = int(input("Digite o ID do registro que deseja excluir: "))
    for item in registros:
        if item["id"] == busca:
            registros.remove(item)
            print("Registro foi excluído com sucesso!")
            return

while True:
    print("-------Menu de regstros-------")
    print("1 - Criar registro")
    print("2 - Listar registros")
    print("3 - Atualizar registro")
    print("4 - Excluir registro")
    print("0 - Sair")
    opcao = input("Escolha uma das opcões: ")

    if opcao == "1":
        criar_registro()
    elif opcao == "2":
        listar_registros()
    elif opcao == "3":
        atualizar_registro()
    elif opcao == "4":
        excluir_registro()
    elif opcao == "0":
       print("Encerrando programa... Até logo!")
       break
    else:
        print("Opção inválida. Tente novamente.")