# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
# ------------------------------------------------------------------------------------------------------------------------------------

# Library import
import math

# Variables
ang = float(input('Digite o valor de um angulo para descobrir qual é o cosseno, seno e tangente desse mesmo angulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

# Final results
print('O seno do angulo de {} é de: {:.2f}' .format(ang, sin))
print('O cosseno do angulo de {} é de: {:.2f}' .format(ang, cos))
print('A tangente do angulo de {} é de: {:.2f}' .format(ang, tan))