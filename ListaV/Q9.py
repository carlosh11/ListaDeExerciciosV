clientes = []


def cadastrar_cliente():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")

    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def pesquisar_cliente():
    nome_pesquisa = input("Digite o nome do cliente: ")

    encontrado = False

    for cliente in clientes:
        if cliente["nome"].lower() == nome_pesquisa.lower():
            print("\nCliente encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            encontrado = True

    if not encontrado:
        print("Cliente não encontrado.")


def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        print("\n--- CLIENTES ---")

        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            print("----------------")


while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar cliente")
    print("2 - Pesquisar cliente pelo nome")
    print("3 - Listar todos os clientes")
    print("4 - Encerrar o programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        pesquisar_cliente()

    elif opcao == "3":
        listar_clientes()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")