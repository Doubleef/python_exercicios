salario = float(input("Digite o valor do Salário atual: R$ "))
novosal = salario + (salario * 15/100)
print("O salário atual é {} R$ e com 15% de aumento o Novo Salário será de {:.2f} R$ ".format(salario, novosal))