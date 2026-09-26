estudantes = []


def cadastrar_estudante():
    nome = input("Digite o nome do estudante: ")
    nota = float(input("Digite a nota: "))

    estudante = {
        "nome": nome,
        "nota": nota
    }

    estudantes.append(estudante)
    print("Estudante cadastrado com sucesso!")


def calcular_media():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    soma = 0

    for estudante in estudantes:
        soma += estudante["nota"]

    media = soma / len(estudantes)

    print(f"Média da turma: {media:.2f}")


def maior_nota():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    maior = estudantes[0]

    for estudante in estudantes:
        if estudante["nota"] > maior["nota"]:
            maior = estudante

    print(f"Estudante com maior nota: {maior['nome']}")
    print(f"Nota: {maior['nota']:.2f}")


def listar_aprovados():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    print("\n--- APROVADOS ---")

    encontrou = False

    for estudante in estudantes:
        if estudante["nota"] >= 7:
            print(f"{estudante['nome']} - Nota: {estudante['nota']:.2f}")
            encontrou = True

    if not encontrou:
        print("Nenhum estudante aprovado.")


while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar estudante")
    print("2 - Exibir média da turma")
    print("3 - Exibir estudante com maior nota")
    print("4 - Listar aprovados")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_estudante()

    elif opcao == "2":
        calcular_media()

    elif opcao == "3":
        maior_nota()

    elif opcao == "4":
        listar_aprovados()

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")