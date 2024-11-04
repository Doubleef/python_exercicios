#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = input(str("Digite a Cidade que você Nasceu: ")).strip() #strip vai tirar espaços antes e depois do que for digitado
print(cid[:5].upper() =="SANTO") #no que for digitado vai procurar até a 5ª posição se é SANTOS

