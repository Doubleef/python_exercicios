#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

#1ª Forma = Maneira Tradicional Matemática sem importação de Classe
co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do Cateto Adjacente: "))
#Hipotenusa = Raiz Quadrada da Soma dos Quadrados dos Catetos
#CO elevado a 2 + CA elevado a 2 e tudo isso elevado a 1/2 raiz quadrada
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A Hipotenusa vai medir: {:.2f}".format(hi))

#2ª Forma = com importação de classe
import math
co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do Cateto Adjacente: "))
hi = (math.hypot(co, ca))
print("O valor da Hipotenusa é de: {:.2f}".format(hi))

#3ª Forma = importanto apenas o Metodo HYPOT
from math import hypot
co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do Cateto Adjacente: "))
hi = hypot(co, ca)
print("O valor da Hipotenusa é de: {:.2f}".format(hi))
