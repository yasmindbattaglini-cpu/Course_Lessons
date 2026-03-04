# Escreva um programa que faça o computador "pensar" em um numeros inteiro entro 0 e 5 e peça para o usuario tentar descobrir
# qual foi o numero escolhifo pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu.

# biblioteca
from random import randint

# pc sorteia um numero
pc = randint(0, 5)

# jogador tenta adivinhar o numeros sorteado pelo pc
print('Estou pensando em um numero. Tente adivinhar...')
jogador = int(input('Em que numero eu pensei? '))

# condicao
if jogador == pc:
    print('Parabens! Voce adivinhou qual numero eu estou pensando!')
else:
    print('Nao foi dessa vez! Eu estava pensando no numero {}!' .format(pc))
