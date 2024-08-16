#Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e
#a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta, pinta uma área de 2m.
alt = float(input("Digite a Altura da Parede:  "))
larg = float(input("Digite a Largura da Parede: "))
area = alt * larg
print('Sua parede tem a dimensão de {} x {} e sua áerea é de: {}m²'.format(alt,larg,area))
tinta = area / 2
print('Para pinta essa parade, você irá precisar de {}Lts de Tinta'.format(tinta))
