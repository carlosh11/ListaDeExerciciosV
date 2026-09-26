def validar_senha(senha):
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True

    if len(senha) >= 8 and tem_maiuscula and tem_minuscula and tem_numero:
        return True
    else:
        return False


while True:
    senha = input("Digite uma senha: ")

    if validar_senha(senha):
        print("Senha válida!")
        break
    else:
        print("Senha inválida! Tente novamente.")