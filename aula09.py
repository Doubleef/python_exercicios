frase = "   Curso em Vídeo Python   "
print(frase)

#FATIAMENTO
print(frase[3]) #imprime apenas a 4 letra que é a s
print(frase[3:13]) #imprime da 4 letra até a letra 13 (no caso imprime até a 12)
print(frase[:13]) #do inicio até o 13
print(frase[13:]) #vai do 13 até o final
print(frase[1:15:2]) #vai imprimir até a 14 pulando de 2 em 2
print(frase[1::2]) #sei o inicio, não sei o final e ele vai imprimir de 2 em 2
print(frase[::2]) #não sei o inicio, não sei o final e ele vai imprimir a string inteira de 2 em 2

#VERIFICAR O TAMANHO DA FRASE
print(len(frase))

#SE EU COLOCAR ESPAÇOS ANTES E DEPOIS DA FRASE O len VAI CONTAR TAMBÉM
print(len(frase))

#SE EU COLOCAR strip ELE VAI REMOVER OS ESPAÇOS ANTES E DEPOIS DA FRASE
print(len(frase.strip()))

#REPLACE - troca uma palavra da frase por outra palavra sugerida
print(frase.replace("Python", "Android"))

#IN - Verifica se algo esta dentro da frase
print("Curso" in frase)

#FIND - procura algo dentro da frase e mostra sua posição
print(frase.find("Vídeo"))

#SPLIT - vai dividir a frase, colocando ela em Lista
print(frase.split())

#SPLIT - ainda com split vou criar uma variável pra me mostrar partes do split
dividido = frase.split()
print(dividido)
print(dividido[2]) #aqui ele vai pegar a posição 2 da divisão feita pelo split
print(dividido[2][3]) #aqui ele vai trazer a letra (e) da posição 2 que é Vídeo

#IMPRIMIR UM TEXTO GRANDE COM APENAS UM PRINT
#COLOCA-SE ASPAS TRIPLAS NO INICIO E NO FIM
print("""Por outro lado, a estrutura atual da
organização representa uma abertura para
a melhoria dos índices pretendidos.""")

