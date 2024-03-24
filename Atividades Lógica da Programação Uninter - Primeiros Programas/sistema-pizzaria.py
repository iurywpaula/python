print('Bem vindo a Pizzaria do Iury de Paula')
print('-' * 21, 'Cardápio', '-' * 22)
print(f'| Código |  Descrição  | Pizza Média | Pizza Grande |')
print(f'|   21   |  Napolitana |     R$ 20,00|      R$ 26,00|')
print(f'|   22   |  Margherita |     R$ 20,00|      R$ 26,00|')
print(f'|   23   |  Calabresa  |     R$ 25,00|      R$ 32,50|')
print(f'|   24   |  Toscana    |     R$ 30,00|      R$ 39,00|')
print(f'|   25   |  Portuguesa |     R$ 30,00|      R$ 39,00|')
print('-' * 53)

tamanho = ''
valor = 0
valor_total = 0
qt_pizza = 0
codigo_pizza = ''
nome_pizza = ''


while True:
    pergunta_tamanho = input('Entre com o tamanho de pizza desejado (M/G): ')

    if pergunta_tamanho not in ('M', 'm', 'G', 'g'):
        print('Opção inválida. Tamanho não existe.')
        continue
    else:
        tamanho = pergunta_tamanho

    while True:
        pergunta_codigo = input('Entre o código da pizza(21/22/23/24/25): ')

        if pergunta_codigo not in ('21', '22', '23', '24', '25'):
            print('Código não existe. Tente novamente com um código válido (21/22/23/24/25)')
            continue

        else:
            codigo_pizza = int(pergunta_codigo)
            break

    if codigo_pizza == 21:
        nome_pizza = 'Napolitana'
        qt_pizza += 1
        if tamanho.lower() == 'm':
            valor = 20;
            valor_total += 20
        elif tamanho.lower() == 'g':
            valor = 26
            valor_total += 26

    elif codigo_pizza == 22:
        qt_pizza += 1
        nome_pizza = 'Margherita'
        if tamanho.lower() == 'm':
            valor = 20;
            valor_total += 20
        elif tamanho.lower() == 'g':
            valor = 26
            valor_total += 26

    elif codigo_pizza == 23:
        qt_pizza += 1
        nome_pizza = 'Calabresa'
        if tamanho.lower() == 'm':
            valor = 25;
            valor_total += 25
        elif tamanho.lower() == 'g':
            valor = 32.50
            valor_total += 32.50

    elif codigo_pizza == 24:
        qt_pizza += 1
        nome_pizza = 'Toscana'
        if tamanho.lower() == 'm':
            valor = 30;
            valor_total += 30
        elif tamanho.lower() == 'g':
            valor = 39
            valor_total += 39
    else:
        nome_pizza = 'Portuguesa'
        qt_pizza += 1
        if tamanho.lower() == 'm':
            valor = 30;
            valor_total += 30
        elif tamanho.lower() == 'g':
            valor = 39
            valor_total += 39

    if qt_pizza > 1:
        print(f'Você pediu {qt_pizza} pizzas. Valor total: R$%.2f' % valor_total)
    else:
        print(f'Você pediu {qt_pizza} pizza. Valor total: R$%.2f' % valor_total)


    mais_pedido = input('Deseja mais uma pizza (S/N): ')

    if mais_pedido.lower() != 's':
        break

print(f'O total do seu pedido ficou: R$%.2f' % valor_total)
