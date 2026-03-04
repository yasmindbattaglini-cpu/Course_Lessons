# Crie um programa qe leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: digite um numero: 6.127. O numero 6,127 tem a parte inteira 6
# --------------------------------------------------------------------------------------------------------------------------------------

#importar biblioteca
import math

# Declaracao de variavel
num = float(input('Digite um número: '))

# importar bibliotec
import math

# Resultado final
print('O valor digitado foi {} e a sua parte inteira é {}' .format(num, math.trunc(num)))