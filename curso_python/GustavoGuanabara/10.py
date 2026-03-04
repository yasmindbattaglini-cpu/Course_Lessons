# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela comprar. Considere que 1 real = 5,9 dolares

# Declaracao de variavel
moeda = float(input('Quantos reais voce tem na carteira? \nR$'))

# Resultado
print ('Com {} reais, você consegue comprar {:.2f} dólares!' .format(moeda, moeda/5.90))