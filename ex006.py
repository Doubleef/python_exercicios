#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
num = int(input("Digite um número: "))
dob = num * 2
trip = num * 3
raiz = num**(1/2)
print("Analisando o valor digitado é {},\n seu DOBRO é: {},\n seu TRIPLO é: {} \n e a sua RAIZ QUADRADA é: {}".format(num, dob, trip, raiz))