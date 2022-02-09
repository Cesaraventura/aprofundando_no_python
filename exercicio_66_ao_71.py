# ex 66 (programa que lê vários números e soma eles e finaliza quando digita 999)
soma = 0
cont = 0
while True:
    num = int(input('digite um numero (digite 999 para finalizar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print('a soma dos valores foi {}!'.format(soma))

# ex 67 (tabuada)
while True:
    n = int(input('digite um numero e descubra sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Fim!')

# ex 69 (analise de dados de grupo)
tot18 = totH = totM20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [m/f] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [s/n] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total de pessoas com mais de 18 anos é {tot18}.')
print(f'ao todo temos {totH} cadastrados.')
print(f'e tempos {totM20} mulheres com menos de 20 anos.')

# ex 70 (estatisticas em produtos)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('nome do produto: '))
    preco = float(input('preco do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in ('SN'):
        resp = str(input('quer continuar?: [s/n] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total da compra foi R${total:.2f}.')
print(f'{totmil} produtos custando mais de 1000 reais.')
print(f'o produto mais barato foi {produto} custando {menor:.2f} reais')

# ex 71 (simulador de caixa eletronico)
valor = int(input('digite o valor que quer sacar: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'o total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
