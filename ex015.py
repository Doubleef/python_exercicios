#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = int(input("Foram quantas Diárias? "))
km = float(input("Quantos Km foram percorridos? "))
val_d = d * 60
val_km = km * 0.15
total = val_d + val_km
print("Foram rodados {} Km em {} dias totalizando um valor de R$ {:.2f}".format(d,km,total))

##PODERIA SER ASSIM TAMBÉM, FORMA MAIS DIRETA
dias = int(input("Foram quantas Diárias? "))
km = float(input("Quantos Km foram percorridos? "))
pago = (dias * 60 + km * 0.15)
print("Foram rodados {} Km em {} dias totalizando um valor de R$ {:.2f}".format(dias,km,pago))