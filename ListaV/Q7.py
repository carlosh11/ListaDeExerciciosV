def analisar_texto(texto):
    total_caracteres = len(texto)
    letras = 0
    numeros = 0
    espacos = 0

    i = 0

    while i < len(texto):
        if texto[i].isalpha():
            letras += 1
        elif texto[i].isdigit():
            numeros += 1
        elif texto[i] == " ":
            espacos += 1

        i += 1

    palavras = len(texto.split())

    return total_caracteres, letras, numeros, espacos, palavras


texto = input("Digite uma frase: ")

resultado = analisar_texto(texto)

print(f"Quantidade total de caracteres: {resultado[0]}")
print(f"Quantidade de letras: {resultado[1]}")
print(f"Quantidade de números: {resultado[2]}")
print(f"Quantidade de espaços: {resultado[3]}")
print(f"Quantidade de palavras: {resultado[4]}")