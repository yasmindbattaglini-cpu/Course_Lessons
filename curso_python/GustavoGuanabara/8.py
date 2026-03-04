# Escreva um programa que leia um valor em metros e ao exiba convertido em centimetros e milimetros

# Declaracao de variavel
num = float(input('Digite um valor em metros: '))

# Conversao de medidas
c = num*100
m = num*1000

# Resultado Final
print('A medida de {} m, corresponde a {} cm e {} mm' .format(num, c, m))
