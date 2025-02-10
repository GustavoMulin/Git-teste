# Pintandp a parede
"""
Este programa calcula a área e a quantidade de litros nescessário para pintar uma parede

Fórmula:
    área = largura * altura
"""

# Definição das dimensões 
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

# Cáculo da área
area = larg * alt

# Exibe o resultado da área
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))

# Cálculo de litros de tinta
tinta = area / 2

# Exibe quantidade
print('Para pintar essa parede você precisará de {}L de tintas'.format(tinta))