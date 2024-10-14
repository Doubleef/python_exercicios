#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#do SENO - COSSENO e TANGENTE desse ângulo.
import math
ângulo = float(input("Digite o Ângulo que você deseja: ")) #o angulo tá em graus, só que a biblioteca math tá em radionos e tem que converter
seno = math.sin(math.radians(ângulo))
print('O Ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print("O Ângulo de {} tem o COSSENHO de {:.2f}".format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print("O Ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, tangente))

#acima importei toda a biblioteca MATH e fiz referência ao modulo que importei.
#abaixo está a forma de importar apenas o que preciso usar do MATH

from math import radians, sin, cos, tan
ângulo = float(input("Digite o Ângulo que você deseja: ")) #o angulo tá em graus, só que a biblioteca math tá em radionos e tem que converter
seno = sin(math.radians(ângulo))
print('O Ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(math.radians(ângulo))
print("O Ângulo de {} tem o COSSENHO de {:.2f}".format(ângulo, cosseno))
tangente = tan(math.radians(ângulo))
print("O Ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, tangente))