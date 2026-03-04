print('Controle Financeiro')

saldo = 0
opcao_inicial=0

while opcao_inicial != 3:
    print('\nOpções que podem ser realizadas: ')
    print('1 - Editar Saldo: ')
    print('2 - Ver Saldo Atual')
    print('3 - Encerrar sessão')

    opcao_inicial=int(input('\nEscolha uma opção: '))

    if opcao_inicial == 1:
        print('1 - Inserir receita')
        print('2 - Inserir despesa')
        print('3 - Voltar')

        opcao_sec=int(input('\nEscolha uma opção: '))

        if opcao_sec == 1:
            valor = float(input("\nDigite o valor da receita: "))
            saldo += valor
            print("Receita registrada com sucesso!")

        elif opcao_sec == 2:
            valor = float(input("\nDigite o valor da despesa: "))
            saldo -= valor
            print("Despesa registrada com sucesso!")

        elif opcao_sec == 3:
            continue

        else:
            print("Opção inválida.")

    if opcao_inicial == 2:
        print(f'\nSaldo atual: R$ {saldo:.2f}')