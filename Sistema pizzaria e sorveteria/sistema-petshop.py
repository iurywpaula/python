# Exercício 3 de 4 da Atividade Prática.
boas_vindas = 'Bem vindo ao Petshop Iury Warszavsky de Paula'

def bordinha(valor):
    print('+', '-' * len(valor), '+')
    print(f'| {valor} |')
    print('+', '-' * len(boas_vindas), '+')

bordinha(boas_vindas)


def cachorro_peso():
    while True:
        try:
            peso_pergunta = float(input('Entre com o peso do cachorro: '))
            valor_peso = peso_pergunta

            if peso_pergunta < 3:
                base = 40
            elif peso_pergunta >= 3 and peso_pergunta < 10:
                base = 50
            elif peso_pergunta >= 10 and peso_pergunta < 30:
                base = 60
            elif peso_pergunta >= 30 and peso_pergunta < 50:\
                base = 70
            else:
                print('Não aceitamos cachorros tão grandes.')
                continue

            return base

        except ValueError:
            print('Você digitou um valor não numérico.')

def cachorro_pelo():
    valor_pelo = 0
    while True:
        pelagem = input('Entre com a pelagem do cachorro\n'
                        'c - Pelo Curto\nm - Pelo Médio\n'
                        'l - Pelo Longo\n'
                        'Pelagem: ')
        if pelagem == 'c':
            multiplicador = 1
        elif pelagem == 'm':
            multiplicador = 1.5
        elif pelagem == 'l':
            multiplicador = 2
        else:
            print('Opção inválida. Insira novamente o tipo de pelagem do cachorro.')
            continue

        valor_pelo = multiplicador
        return multiplicador, valor_pelo

def cachorro_extra():
    extra = 0
    while True:
        servico_extra = input('Deseja adicionar mais algum servico?\n'
                              '1 - Corte de Unhas - R$ 10,00\n'
                              '2 - Escovar Dentes - R$ 12,00\n'
                              '3 - Limpeza de Orelhas - R$ 15,00\n'
                              '0 - Não desejo mais nada\n'
                              'Resposta: ')
        if servico_extra == '1':
            extra += 10
        elif servico_extra == '2':
            extra += 12
        elif servico_extra == '3':
            extra += 15
        elif servico_extra == '0':
            return extra
        else:
            print('Você inseriu um valor inválido. Tente novamente.')
            continue

base = cachorro_peso()
multiplicador, valor_pelo = cachorro_pelo()
extra = cachorro_extra()
total = base * multiplicador + extra

print(f'Total a pagar(R$): %.2f (Peso: {base} x pelagem: {valor_pelo}  + adicional(is): {extra})' % total)