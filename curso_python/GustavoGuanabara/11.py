''''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta
necessaria para pinta-la, sabendo q acada litro de tinta, pinta uma area de 2m²
'''

# Declaracao de variavel
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

# Conta
area = altura * largura
tinta = area/2

# Resultado
print ('Como a área da sua parede é de {:.3} m², você vai precisar de {:.3} litros de tinta para pintar a sua parede' .format(area, tinta))