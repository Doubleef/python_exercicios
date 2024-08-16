#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar.
real = float(input("Quando você tem na Carteira? R$ "))
dolar = real / 5.72
print('Com R$ {:.2f} Você pode comprar {:.2f} U$ Dolares'.format(real, dolar))