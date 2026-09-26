def calcular_medias(notas):
    return sum(notas) / len(notas)


estudantes = {}

while True:
    nome = input("Digite o nome do estudante: ")

    notas = []

    for i in range(3):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)

    estudantes[nome] = notas

    continuar = input("Deseja cadastrar outro estudante? (s/n): ")

    if continuar.lower() != "s":
        break


print("\nResultado dos estudantes:")

for nome, notas in estudantes.items():
    media = calcular_medias(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"Nome: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print()