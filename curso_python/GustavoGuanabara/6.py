# Crie um algoritmo ue leia um numero e mostre o seu dobro, triplo e raiz quadradda
num = int(input('Digite um número: ')) # declaracao de variavel

d = num*2 # calcula o dobro do valor
t = num*3 # calcula o triplo do valor
rq = num ** (1/2) # calcula a raiz quadrada. Aqui tem q lembrar das aulas de matematica, q um numero elevado a uma fraçao pode ser reescrito como raiz quadrada do inverso da fração

print ('O dobro do valor é {} \n o triplo do valor é {} \n a raiz quadrada do valor é {}' .format(d, t, rq))