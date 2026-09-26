tarefas = []


def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")


def listar_tarefa():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i} - {tarefa}")


def remover_tarefa():
    listar_tarefa()

    if len(tarefas) > 0:
        numero = int(input("Digite o número da tarefa que deseja remover: "))

        if numero >= 1 and numero <= len(tarefas):
            tarefas.pop(numero - 1)
            print("Tarefa removida!")
        else:
            print("Número inválido.")


while True:
    print("\n--- MENU ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        listar_tarefa()

    elif opcao == "3":
        remover_tarefa()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")