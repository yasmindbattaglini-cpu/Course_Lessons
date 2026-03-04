# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

# Declaracao das variaveis
salario = float(input('Digite o valor do sálario do funcionário: R$ '))

# conta
reajuste = salario + salario*15/100

# Resultado
print('Com o reajuste salarial de 15%, o sálario de R$ {:.2f} passa a ser R$ {:.2f}' .format(salario, reajuste))