# Escreva um programa que converta uma temperatura digitada em ºC para ºF

# Declarando as variaveis
celsius = float(input('Digite a temperatura em graus Celsius: '))

# Conversao
f = celsius*1.8+32

# Resultado final
print('A temperatura de {}ºC corresponde a {} F' .format(celsius, f))