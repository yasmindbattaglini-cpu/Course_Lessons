# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre 
# o comprimento da hipotenusa

# ------------------------------------------------------------------------------------------------------------------------------------

# Importar biblioteca
import math

# variavel
co = float(input('Digite o complimento do valor do cateto oposto do triangulo retangulo: '))
ca = float(input('Digite o complimento do valor do cateto adjacente do triangulo retangulo: '))
hi = math.hypot(co, ca)

# resultado final
print('A hipotenusa tem um comprimento de {:.2f}'.format(hi))