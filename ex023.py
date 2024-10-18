#Faça um programa que leia um número de 0 a 9999 e mostre na tela
#cada um dos dígitos separados.

num = int(input("Digite um número: "))
u = num // 1 % 10 #divide por um e depois faz modulo de 10 (resto da Divisão)
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisando o Número {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
