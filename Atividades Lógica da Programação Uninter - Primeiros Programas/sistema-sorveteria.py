# Mensagem de boas vindas com meu nome, Iury de Paula (RU de aluno: 4571817)
print('Bem vindo a Sorveteria do Iury de Paula')
print('-' * 36, 'Cardápio', '-' * 36)
print('|', 'N° DE BOLAS', '|', 'Sabor Tradicional (tr)', '|', 'Sabor Premium (pr)', '|', 'Sabor Especial(es)', '|')
print('|', '     1     ', '|', '        R$ 6,00       ', '|', '      R$ 7,00      ' '|', '     R$ 8,00      ', '|')
print('|', '     2     ', '|', '        R$ 11,00      ', '|', '      R$ 13,00     ' '|', '     R$ 15,00     ', '|')
print('|', '     3     ', '|', '        R$ 15,00      ', '|', '      R$ 18,00     ' '|', '     R$ 21,00     ', '|')

print('-' * 82)

sabor = ''
nome_sabor = ''
bolas = 0
valor = 0
valor_total = 0

 
 

while True:

    # validando se o sabor foi digitado corretamente.
    while True:
        pergunta_sabores = input('Entre com o sabor desejado (tr/pr/es): ')

        if pergunta_sabores not in ('tr', 'pr', 'es'):
            print('Sabor inválido. Tente novamente.')
            continue

        else:
            # Armazenando a resposta válida na variável sabor.
            sabor = pergunta_sabores
            break


    # validando se o numero de bolas de sorvete foi digitado corretamente.
    while True:
        pergunta_bolas = input('Entre com o número de bolas de sorvete desejado(1/2/3): ')

        if pergunta_bolas not in ('1', '2', '3'):
            print('Número de bolas de sorvete inválido. Tente novamente.')
            continue

        else:
            # Armazenando a resposta válida na variável bolas e convertendo-a em numero inteiro.
            bolas = int(pergunta_bolas)
            break

    # Crio uma condição onde SE o sabor for sabor Tradicional, SE for 1 bola, o valor será X, assim para cada bola e cada sabor.

    if (sabor == 'tr'):
        nome_sabor = 'TRADICIONAL'  # A variável nome_sabor recebe o nome do sabor para imprimir antes de finalizar o pedido.

        if (bolas == 1):
            # Atualizamos o valor da variável "valor" e criamos uma soma da variavel valor_total, para sempre que a condição for true, ela somar esse valor no valor_total.
            valor = 6
            valor_total += 6

        elif (bolas == 2):
            valor = 11
            valor_total += 11

        else:
            valor = 15
            valor_total += 15


    elif (sabor == 'pr'):
        nome_sabor = 'PREMIUM'

        if (bolas == 1):
            valor = 7
            valor_total += 7

        elif (bolas == 2):
            valor = 13
            valor_total += 13

        else:
            valor = 18
            valor_total += 18

 
 

    else:
        nome_sabor = 'ESPECIAL'
        if (bolas == 1):
            valor = 8
            valor_total += 8

        elif (bolas == 2):
            valor = 15
            valor_total += 15

        else:
            valor = 21
            valor_total += 21

    # Imprimimos uma frase com o número de bolas, sabor e preço até o dado momento. Há uma condição que torna a frase mais harmoniosa com a quantidade de bolas.

    if (bolas > 1):
        print(f'Você pediu {bolas} bolas de sorvete no sabor {nome_sabor}: R$ %.2f' % valor_total)
    else:
        print(f'Você pediu {bolas} bola de sorvete no sabor {nome_sabor}: R$ %.2f' % valor_total)

 
 

    # Agora vamos validar se o cliente deseja mais sorvete ou se será somente um único pedido antes de fecharmos a conta.
    mais_pedido = input('Deseja mais algum sorvete (s/n): ')

    if (mais_pedido.lower() != 's'):
        break

# Imprimimos uma frase com o número total do pedido.

print(f'O total do seu pedido é: R$ %.2f' % valor_total)
