#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input("Digite um número: "))
ant = (num -1)
suc = (num +1)
print("Analisando o valor digitado é {}, seu ANTECESSOR é: {}  e o SUCESSOR é: {}".format(num, ant, suc))
