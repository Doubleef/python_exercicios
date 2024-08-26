#IMPORTANDO MODULOS

#Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção Inteira.
#1ª forma --> aqui o import esta trazendo tudo que é da biblioteca MATH
import math
num = float(input("Digite um número: "))
print("O número digitado foi {} e a sua porção inteira é: {}".format(num, math.trunc(num)))


#2ª forma --> aqui o import traz apenas o TRUNC
from math import trunc
num = float(input("Digite um número: "))
print("O número digitado foi {} e a sua porção inteira é: {}".format(num, trunc(num)))


#3ª forma --> aqui eu utilizo uma Função, no caso o INT vai mostrar o inteiro do número digitado
num = float(input("Digite um número: "))
print("O número digitado foi {} e a sua porção inteira é: {}".format(num, int(num)))
