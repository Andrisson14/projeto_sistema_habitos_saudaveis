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
            print()
    else:
        print("Nenhum registro encontrado.")

def atualizar_registro():
    busca = int(input("Digite o ID do registro que deseja atualizar:"))
    for item in registros:
        if item ["id"] == busca:
            item["id_usuario"] = int(input("Novo ID do usuário: "))
            item["id_habito"] = int(input("Novo ID do hábito: "))
            item["data"] = input("Nova data (dd/mm/aaaa): ")
            item["realizado"] = input("Realizado? (Sim/Não): ")
            print("Registro atualizado com sucesso!")
            print()
            return

def excluir_registro():
    busca = int(input("Digite o ID do registro que deseja excluir: "))
    for item in registros:
        if item["id"] == busca:
            registros.remove(item)
            print("Registro foi excluído com sucesso!")
            print()
            return

def procurar_registro():
    busca = int(input("Digite o ID do registro que deseja procurar: "))
    for item in registros:
        if item["id"] == busca:
            print("ID do usuario:", item["id_usuario"])
            print("ID do hábito:", item["id_habito"])
            print("Data:", item["data"])
            print("Realizado:", item["realizado"])
            print()
            return
    else:
        print("Registro não encontrado.")
           

while True:
    print("-------Menu de regstros-------")
    print()
    print("1 - Criar registro")
    print("2 - Listar registros")
    print("3 - Procurar registro")
    print("4 - Excluir registro")
    print("5 - Atualizar registro")
    print("0 - Sair")
    opcao = input("Escolha uma das opcões: ")

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