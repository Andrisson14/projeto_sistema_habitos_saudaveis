from arquivos import carregar_dados


ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_HABITOS = "habitos.json"


def relatorio_geral():
    
    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    habitos = carregar_dados(ARQUIVO_HABITOS)

    print("\n" + "=" * 50)
    print("📊 RELATÓRIO GERAL DO SISTEMA")
    print("=" * 50)

    print(f"\n👥 Total de usuários: {len(usuarios)}")
    print(f"🎯 Total de hábitos: {len(habitos)}")

    print("\n📂 Distribuição por categoria:")
    
    categorias = {}
    for habito in habitos:
        categoria = habito["categoria"]
        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += 1

    if len(categorias) == 0:
        print("   Nenhuma categoria cadastrada ainda.")
    else:
        for categoria in categorias:
            quantidade = categorias[categoria]
            print(f"   • {categoria}: {quantidade} hábito(s)")

    print("\n" + "=" * 50 + "\n")


def relatorio_usuario():
    
    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    habitos = carregar_dados(ARQUIVO_HABITOS)

    print("\n" + "=" * 50)
    
    while True:
        try:
            id_usuario = int(input("Digite o ID do usuário: "))
            break
        except ValueError:
            print("❌ Erro! Digite um número válido.")

    usuario_encontrado = None
    
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print(f"❌ Usuário com ID {id_usuario} não encontrado.\n")
        return

    print("\n📋 RELATÓRIO DO USUÁRIO")
    print("-" * 50)
    
    print(f"📛 Nome: {usuario_encontrado['nome']}")
    print(f"🎂 Idade: {usuario_encontrado['idade']} anos")
    print(f"⚖️  Peso: {usuario_encontrado['peso']} kg")
    print(f"📏 Altura: {usuario_encontrado['altura']} m")

    print("\n🎯 Hábitos cadastrados:")
    print("-" * 50)
    
    habitos_encontrados = 0
    
    for habito in habitos:
        if habito["id_usuario"] == id_usuario:
            habitos_encontrados += 1
            print(f"\n   {habitos_encontrados}. {habito['nome']}")
            print(f"      Categoria: {habito['categoria']}")
            print(f"      Meta diária: {habito['meta_diaria']}")

    if habitos_encontrados == 0:
        print("   Nenhum hábito cadastrado para este usuário.")

    print("\n" + "=" * 50 + "\n")

def relatorio_completo_usuario():

    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    habitos = carregar_dados(ARQUIVO_HABITOS)
    registros = carregar_dados("registros.json")

    print("\n" + "=" * 50)
    print("📊 RELATÓRIO COMPLETO DO USUÁRIO")
    print("=" * 50)

    try:
        id_usuario = int(input("Digite o ID do usuário: "))
    except ValueError:
        print("❌ ID inválido.")
        return

    usuario = None
    for u in usuarios:
        if u["id"] == id_usuario:
            usuario = u
            break

    if usuario is None:
        print("❌ Usuário não encontrado.")
        return

    print(f"\n👤 Usuário: {usuario['nome']}")

    print("\n🎯 Desempenho por hábito:")
    print("-" * 50)

    encontrou_habito = False

    for habito in habitos:
        if habito["id_usuario"] == id_usuario:

            encontrou_habito = True
            total = 0
            realizados = 0

            for r in registros:
                if r["id_usuario"] == id_usuario and r["id_habito"] == habito["id"]:
                    total += 1

                    if str(r["realizado"]).lower() == "sim":
                        realizados += 1

            if total > 0:
                taxa = (realizados / total) * 100
            else:
                taxa = 0

            print(f"\n📌 {habito['nome']}")
            print(f"   Categoria: {habito['categoria']}")
            print(f"   Meta: {habito['meta_diaria']}")
            print(f"   Registros: {total}")
            print(f"   Concluídos: {realizados}")
            print(f"   Taxa de sucesso: {taxa:.2f}%")

    if not encontrou_habito:
        print("Nenhum hábito cadastrado para este usuário.")

    print("\n" + "=" * 50 + "\n")

def menu_relatorios():

    while True:

        print("\n===== RELATÓRIOS =====")
        print("1 - Relatório geral")
        print("2 - Relatório por usuário")
        print("3 - Relatório completo do usuário")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            relatorio_geral()

        elif opcao == "2":
            relatorio_usuario()
        
        elif opcao == "3":
            relatorio_completo_usuario()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

