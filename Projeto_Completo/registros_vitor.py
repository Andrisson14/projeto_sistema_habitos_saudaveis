from arquivos import carregar_dados, salvar_dados
from datetime import datetime

ARQUIVO = "registros.json"
ARQUIVO_HABITOS = "habitos.json"
ARQUIVO_USUARIOS = "usuarios.json"


def criar_registro():

    registros = carregar_dados(ARQUIVO)
    habitos = carregar_dados(ARQUIVO_HABITOS)
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
        entrada = input("Habito ID: ").strip()
        try:
            id_habito = int(entrada)
        except ValueError:
            print("Você deve digitar um número.")
            continue
        if id_habito <= 0:
            print("Número inválido! O número deve ser maior que 0.")
            continue
        if not any(int(h["id"]) == id_habito for h in habitos):
            print("Hábito não encontrado! Digite um ID de hábito existente.")
            continue
        break

    while True:
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
    
    novo_id = max((item["id"] for item in registros), default=0) + 1

    

    registro = {
        "id": novo_id,
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
        print("\nLista de Registros: ")
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

                        salvar_dados(ARQUIVO, registros)
                        print("Registro atualizado com sucesso!")
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

                        salvar_dados(ARQUIVO, registros)
                        print("Registro foi excluído com sucesso!")
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
            
