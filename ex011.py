alt = float(input("Digite a Altura da Parede:  "))
larg = float(input("Digite a Largura da Parede: "))
area = alt * larg
print('Sua parede tem a dimensão de {} x {} e sua áerea é de: {}m²'.format(alt,larg,area))
tinta = area / 2
print('Para pinta essa parade, você irá precisar de {}Lts de Tinta'.format(tinta))
