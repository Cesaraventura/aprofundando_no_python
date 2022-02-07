# ex 57
sexo = str(input('informe seu sexo: [M/F] ')).strip().upper()[0] #fiz o fatiamento para escolher so a primeira letra caso ele escreve algo com mais letras
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos. por favor, informe seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))

# ex 58
from random import randint
computador = randint(0, 10)
print('sou seu computador... acabei de pensar em um numero de 0 a 10.')
print('sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('menos... tente mais uma vez.')
print('acertou com {} tentativas. Parabens!'.format(palpites))

# ex 59
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''   [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('qual sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('a soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('o produto entre {} e {} é {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('informe os valores novamente:')
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('opcao invalida. tente novamente!')
print('fim do programa! volte sempre!')

# ex 60
n = int(input('digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
