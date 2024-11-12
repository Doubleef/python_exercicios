#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Digite seu nome completo: ")).strip()
nome = n.split() #aqui ele vai "fatiar" o nome e colocar em uma lista
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é {}".format(nome[len(nome)-1])) #aqui ele vê o tamanho de nome e coloca o último menos 1




