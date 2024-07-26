def calculadora():
    while True:
        print('Calculadora Simples')
        print()
        print('1. Soma')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('5. Sair')

        operacao = input('Escolha a opção desejada: ')

        if operacao == '5':
            print('Obrigado por utilizar a Calculador Simples!')
            break

        if operacao not in ['1', '2', '3', '4']:
            print('Opção inválida, por favor, coloque uma opção válida.')
            continue

        numero_1 = float(input('Primeiro número: '))
        numero_2 = float(input('Segundo número: '))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print(f'O resultado da operação soma é: ${resultado}')
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print(f'O resultado da operação subtração é: ${resultado}')
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print(f'O resultado da operação multiplicação é: ${resultado}')
        else:
            if numero_2 == 0:
                print('Divisões por zero não são possíveis, tente novamente.')
                continue
            else:
                resultado = numero_1 / numero_2
                print(f'O resultado da operação divisão é: ${resultado}')

calculadora()            