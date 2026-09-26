def calcular_total(carrinho):
    total = 0

    for produto in carrinho:
        total += produto["quantidade"] * produto["preco"]

    return total


carrinho = []

while True:
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: R$ "))

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    carrinho.append(produto)

    continuar = input("Deseja cadastrar outro produto? (s/n): ")

    if continuar.lower() != "s":
        break


print("\nProdutos do carrinho:")

for produto in carrinho:
    print(f"{produto['nome']} - Quantidade: {produto['quantidade']} - "
          f"Preço: R$ {produto['preco']:.2f}")

total = calcular_total(carrinho)

print(f"\nTotal da compra: R$ {total:.2f}")