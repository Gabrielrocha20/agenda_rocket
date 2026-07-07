contatos = []


def menu():
    print("\n" + "=" * 40)
    print("         AGENDA DE CONTATOS")
    print("=" * 40)
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Editar contato")
    print("4 - Favoritar/Desfavoritar contato")
    print("5 - Listar favoritos")
    print("6 - Excluir contato")
    print("0 - Sair")
    print("=" * 40)


def adicionar_contato():
    print("\n=== Novo Contato ===")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }

    contatos.append(contato)

    print("\n✅ Contato cadastrado com sucesso!")


def listar_contatos():

    if len(contatos) == 0:
        print("\nNenhum contato cadastrado.")
        return

    print("\n===== CONTATOS =====")

    for indice, contato in enumerate(contatos):

        estrela = "★" if contato["favorito"] else " "

        print(f"""
[{indice}]
Nome      : {contato["nome"]}
Telefone  : {contato["telefone"]}
Email     : {contato["email"]}
Favorito  : {estrela}
------------------------------
""")


def editar_contato():

    if len(contatos) == 0:
        print("\nNenhum contato cadastrado.")
        return

    listar_contatos()

    try:
        indice = int(input("Digite o índice do contato: "))

        if indice < 0 or indice >= len(contatos):
            print("Índice inválido.")
            return

        print("\nDigite os novos dados:")

        contatos[indice]["nome"] = input("Nome: ")
        contatos[indice]["telefone"] = input("Telefone: ")
        contatos[indice]["email"] = input("Email: ")

        print("\n✅ Contato atualizado!")

    except ValueError:
        print("Digite um número válido.")


def favoritar():

    if len(contatos) == 0:
        print("\nNenhum contato cadastrado.")
        return

    listar_contatos()

    try:

        indice = int(input("Escolha o contato: "))

        if indice < 0 or indice >= len(contatos):
            print("Índice inválido.")
            return

        contatos[indice]["favorito"] = not contatos[indice]["favorito"]

        if contatos[indice]["favorito"]:
            print("⭐ Contato favoritado!")
        else:
            print("Contato removido dos favoritos!")

    except ValueError:
        print("Digite um número válido.")


def listar_favoritos():

    favoritos = [contato for contato in contatos if contato["favorito"]]

    if len(favoritos) == 0:
        print("\nNenhum favorito cadastrado.")
        return

    print("\n===== FAVORITOS =====")

    for contato in favoritos:

        print(f"""
Nome      : {contato["nome"]}
Telefone  : {contato["telefone"]}
Email     : {contato["email"]}
⭐ Favorito
------------------------------
""")


def excluir_contato():

    if len(contatos) == 0:
        print("\nNenhum contato cadastrado.")
        return

    listar_contatos()

    try:

        indice = int(input("Digite o índice do contato: "))

        if indice < 0 or indice >= len(contatos):
            print("Índice inválido.")
            return

        nome = contatos[indice]["nome"]

        contatos.pop(indice)

        print(f"\n🗑️ Contato '{nome}' removido com sucesso!")

    except ValueError:
        print("Digite um número válido.")


while True:

    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()

    elif opcao == "2":
        listar_contatos()

    elif opcao == "3":
        editar_contato()

    elif opcao == "4":
        favoritar()

    elif opcao == "5":
        listar_favoritos()

    elif opcao == "6":
        excluir_contato()

    elif opcao == "0":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida.")
