# ex 36
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pegar um casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('emprestimo pode ser CONCEDIDO!')
else:
    print('emprestimo NEGADO!')

# ex 37
num = int(input('digite um numero inteiro: '))
print('''escolha uma das bases para conversao:
      [ 1 ] converter para binario
      [ 2 ] converter para octal
      [ 3 ] converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida. tente novamente')

# ex 38
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
if n1 > n2:
    print('o primeiro valor é maior')
elif n2 > n1:
    print('o segundo valor é maior')
else:
    print('os dois valores sao iguais')

# ex 39
from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print ('voce tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))

# ex 40
nota1 = float(input('primeira nota:'))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print('tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('o aluno esta em recuperacao.')
elif media < 5:
    print('o aluno esta reprovado.')
elif media >= 7:
    print('o aluno esta aprovado.')

# ex 41
atual = date.today().year
nascimento = int(input('ano de nascimento: '))
idade = atual - nascimento
print('o atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('mirim')
elif idade <= 14:
    print('infantil')
elif idade <= 19:
    print('junior')
elif idade <= 25:
    print('senior')
else:
    print('master')

# ex 42
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('os segmentos acima podem formar um triangulo', end=' ')
    if r1 == r2 == r3:
        print('equilatero')
    elif r1 != r2 != r3 != r1:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('os segmentos nao podem formar um triangulo')

# ex 43
peso = float(input('qual seu peso?'))
altura = float(input('qual sua altura?'))
imc = peso / (altura ** 2)
print('o imc essa pessoa é {:.2f}'.format(imc))
if imc < 18.5:
    print('voce esta abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('voce esta no peso normal')
elif 25 <= imc < 30:
    print('voce esta sobrepeso')
elif 30 <= imc < 40:
    print('voce esta obeso')
else:
    print('OBESIDADE MORBIDA')

# ex 44
print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('preco das compras: R$'))
print('''formas de pagamento
[ 1 ] a vista dinheiro
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('qual a opcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('sua compra sera parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('quantas parcelas?'))
    parcela = total / totparc
    print('sua compra sera parcelada em {}x de R${:.2f} com juros.'.format(preco, total))
else:
    total = preco
    print('opcao invalida de pagamento. tente novamente!')
print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))

# ex 45
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opcoes:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('qual sua jogada'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' * 11)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida')
