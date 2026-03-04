## Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome deles e escrevendo o nome do escolhido

# Importar biblioteca random
import random

# Declarando as variaveis
nome1 = str(input('Digite seu nome: '))
nome2 = str(input('Digite seu nome: '))
nome3 = str(input('Digite seu nome: '))
nome4 = str(input('Digite seu nome: '))

lista = [nome1, nome2, nome3, nome4]

escolhido = random.choice(lista)

print('O aluno escolhido para apagar a lousa foi o {}' .format(escolhido))