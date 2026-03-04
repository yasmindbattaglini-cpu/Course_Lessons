# O mesmo professor do desafio anterior quer sortear a aordem de aparesentacao de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.

# Importando a biblioteca
import random

# Variaveis
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

# organizando em lista
lista =[nome1, nome2, nome3, nome4]

# randomizando a lista
random.shuffle(lista)

# resultado final
print('A ordem de apresentação dos trabalho é ')
print(lista)