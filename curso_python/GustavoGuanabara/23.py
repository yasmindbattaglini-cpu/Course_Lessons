# Faça um programa que lia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#Ex: 1834; unidade = 4, dezena = 3, centena = 8, milhar = 1

# Declarando variavel 
num = int(input('Digite um valor de um numero de 0 a 9999: '))

n = str(num)

print('Analisando o numero {}' .format(num))
print('Milhar: {}' .format(n[0]))
print('Centena: {}' .format(n[1]))
print('Dezena: {}' .format(n[2]))
print('Unidade: {}' .format(n[3]))

