#Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = input(str("Digite seu nome Completo: ")).strip()
print("Analisando seu nome:...")
print("Seu nome em Maiusculas é: {}".format(nome.upper()))
print("Seu nome em Minusculas é: {}".format(nome.lower()))
print("A Quantidade de Letras do seu nome são: {}".format(len(nome) -nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))

#outra forma de fazer seria:
separa = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))

