preco = float(input("Digite o preço do Produto: R$ "))
novo = preco - (preco * 5/100)
print("O preço do produto é: {} na promoção com o desconto de 5% vai custar por {:.2f}".format(preco, novo))
