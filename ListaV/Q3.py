def contar_palavras(frase):
    frase = frase.lower()
    palavras = frase.split()

    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem


frase = input("Digite uma frase: ")

resultado = contar_palavras(frase)

print(resultado)