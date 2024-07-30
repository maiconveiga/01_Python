
while(True):
    n1 = int(input('Insira um valor: '))
    n2 = int(input('Insira outro valor: '))



    print('Escolha a operação:')
    print('1 - Soma:')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4 - Multiplicação')
    o = int(input('Insira o número da opção: '))

    if o == 1:
        print('Resultado: ', n1 + n2)
    elif o == 2:
        print('Resultado: ', n1 - n2)
    elif o == 3:
        print('Resultado: ', n1 / n2)
    elif o == 4:
        print('Resultado: ', n1 * n2)
    else:
        print('Opção inválida')
    