from habitos_isaque import criar_habito, ler_todos_habitos, ler_um_habito, editar_habito, excluir_habito
from registros_vitor import criar_registro, listar_registros, procurar_registro, atualizar_registro, excluir_registro
from usuarios_rafael import cadastrar_usuario, listar_usuarios, buscar_usuario, atualizar_usuario, excluir_usuario
from relatorios_paulo import menu_relatorios

def menu_usuarios():
    while True:
        print("========== MENU – USUÁRIOS ==========")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Buscar usuário por ID")
        print("4. Atualizar usuário")
        print("5. Excluir usuário")
        print("6. Voltar")
        print("======================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            atualizar_usuario()
        elif opcao == "5":
            excluir_usuario()
        elif opcao == "6":
            break
        else:
            print("Opção inválida!\n")

def menu_habitos():
    while True:
        print("========== MENU – HÁBITOS ==========")
        print("1. Cadastrar novo hábito")
        print("2. Listar todos os hábitos")
        print("3. Buscar hábito por ID")
        print("4. Atualizar hábito")
        print("5. Excluir hábito")
        print("6. Voltar")
        print("=====================================")

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
            break
        else:
            print("Opção inválida!\n")

def menu_registros():
    while True:
        print("========== MENU – REGISTROS DIÁRIOS ==========")
        print("1. Adicionar novo registro")
        print("2. Listar todos os registros")
        print("3. Buscar registro por ID")
        print("4. Atualizar registro")
        print("5. Excluir registro")
        print("6. Voltar")
        print("===============================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_registro()
        elif opcao == "2":
            listar_registros()
        elif opcao == "3":
            procurar_registro()
        elif opcao == "4":
            atualizar_registro()
        elif opcao == "5":
            excluir_registro()
        elif opcao == "6":
            break
        else:
            print("Opção inválida!\n")

def exibir_menu():
    while True:
        print("\n╔══════════════════════════════════════════════╗")
        print("║       SISTEMA DE HÁBITOS SAUDÁVEIS            ║")
        print("║                 HABIT FLOW                    ║")
        print("╠══════════════════════════════════════════════╣")
        print("║  1. Usuários                                  ║")
        print("║  2. Hábitos                                   ║")
        print("║  3. Registros Diários                         ║")
        print("║  4. Relatórios de Evolução                    ║")
        print("║  5. Sair                                      ║")
        print("╚══════════════════════════════════════════════╝")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_usuarios()
        elif opcao == "2":
            menu_habitos()
        elif opcao == "3":
            menu_registros()
        elif opcao == "4":
            menu_relatorios()
        elif opcao == "5":
            print("Saindo... até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")





