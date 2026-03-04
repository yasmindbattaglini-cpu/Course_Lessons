'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carros custa R$60,00 por dia e R$0,15 por km rodado.
'''

# Declaracao de variaveis
dias = int(input('Por quantos dias o carro foi alugado? \n'))
km = float(input('O carro percorreu quantos km? \n'))

# Conta
total_dia = dias * 60
total_km = km * 0.15
total = total_dia + total_km

# Resultado final
print('Como o carro foi rodado por {} dias e percorreu uma distância de {} km, você deve pagar um valor de R$ {:.2f}' .format(dias, km, total))