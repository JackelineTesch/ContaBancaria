from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

cliente_conta_corrente = ContaCorrente(None, 0.0, 500.00)
cliente_poupanca = ContaPoupanca(None, 500.00, 6.17)

while True:
    print("Bem vindo ao banco Cuidando do seu dinheiro!" )
    print("1 - Conta Corrente")
    print("2 - Poupança")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Voltar")
        opcao_conta_corrente = int(input("Digite a opção desejada: "))
        if opcao_conta_corrente == 1:
            valor = float(input("Digite o valor desejado: "))
            cliente_conta_corrente.sacar(valor)
        elif opcao_conta_corrente == 2:
            valor = float(input("Digite o valor a ser depositado: "))
            cliente_conta_corrente.depositar(valor)                       
        elif opcao_conta_corrente == 3:
            continue
        else:
            print("Opção inválida! \n")
    elif opcao == 2:
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Verificar rendimento")
        print("4 - Voltar")
        opcao_poupanca = int(input("Digite a opção desejada: "))
        if opcao_poupanca == 1:
            valor = float(input("Digite o valor desejado: "))
            ContaPoupanca.sacar(cliente_poupanca, valor)
        elif opcao_poupanca == 2:
            valor = float(input("Digite o valor a ser depositado: "))
            ContaPoupanca.depositar(cliente_poupanca, valor)
        elif opcao_poupanca == 3:
            unidade_de_tempo = input("Digite a unidade de tempo da aplicação (dias, meses ou anos):")
            tempo_de_aplicacao = int(input(f"Digite o tempo da aplicação:"))
            ContaPoupanca.verificar_rendimento(cliente_poupanca, unidade_de_tempo, tempo_de_aplicacao)
        elif opcao_poupanca == 4:
            continue
        else: 
            print("Opção inválida!")
    elif opcao == 3:
        print("Obrigado por utilizar nossos serviços!")
        break
    else:
        print("Opção inválida!")
        
    
    
        