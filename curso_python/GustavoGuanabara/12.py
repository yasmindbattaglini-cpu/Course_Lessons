# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

# Declarando variaveis
preço = float(input('Digite o valor do produto: R$'))

# Conta 
novo_preço = preço - preço*5/100

# Resultado final
print ('O produto de R${} está saindo por R${}, pois esta tendo uma promoção de 5% de desconto!' .format(preço, novo_preço))