#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = int(input("Digite a Primeira Nota: "))
n2 = int(input("Digite a Segunda Nota: "))
soma = (n1 + n2)
media = (soma / 2)
print( "Sua NOTA 01 foi: {}\n Sua NOTA 02 foi: {}\n Totalizando: {}\n e você ficou com MÉDIA: {}".format(n1, n2, soma, media))