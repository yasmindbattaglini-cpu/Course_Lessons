smtg = input('Digite alguma coisa: ')

print('O tipo primitivo desse valor é de: ', type(smtg))
print('Só tem espaço? ', smtg.isspace()) 
print('É um número? ', smtg.isnumeric())
print('É alfabético? ', smtg.isalpha())
print('Esta em maiusculo? ', smtg.isupper())
print('Esta em minusculo? ', smtg.islower())