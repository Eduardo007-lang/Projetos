larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg*alt
print('Sua parede tem {}x{} e a sua area é {}m'.format(larg, alt, area), end =' ')
tinta = area / 2
print('Para pintar essa área voce precisa de {}L de tinta'.format(tinta))
