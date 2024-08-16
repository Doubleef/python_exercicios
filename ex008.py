#Escreva um programa que leiA um valor em metros e o exiba convertido em centrimetros e milimetros.
medida = float(input("Uma distância em Metros: "))
cm = medida * 100
mm = medida * 1000
print( "O valor em METROS foi: {}\n Convertido para CENTIMETROS dá: {:.0f}\n e em MILIMETROS é igual a: {:.0f}".format(medida, cm, mm))


