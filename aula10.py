"""nome = str(input("Digite seu nome: "))
if nome == "Flávio":
    print("Seu nome é tão lindo")
else:
    print("Seu nome é tão comum")
print("Bom dia {}".format(nome))"""

#----------------------------------------------------------

n1 = float(input("Digite a nota 01: "))
n2 = float(input("Digite a nota 02: "))
m = (n1 + n2)/2
print("A sua média foi: {:.1f}".format(m))
if m >= 6.0:
    print("Você foi aprovado. PARABÉNS")
else:
    print("Sua nota foi baixa. ESTUDE MAIS")


