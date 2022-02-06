# ex 47
for n in range(2, 51, 2): #(primeiro numero é onde começa, o segundo é onde termina e o terceiro é quanto pula)
    print(n, end=' ')
print('acabou')

# ex 48
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:  # % = divisivel
        cont = cont + 1
        soma = soma + c
print('a soma de todos os {} valores solicitados é {}'.format(cont, soma))

# ex 49
num = int(input('digite um numero para ver sua tabuada: '))
for c in range(1, 11): # colocando até o 11, ele vai de 1 a 10
    print('{} x {:2} = {}'.format(num, c, num*c))

# ex 50
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite o {} valor: '.format(c)))
    if num % 2 == 0:    # % 2 == 0 -> mostra que ele é divisivel por 2 e o resto é 0
        soma += num   # += é como se fosse soma = soma + num
        cont += 1
print('voce escreveu {} numeros pares e a soma entre eles foi {}'.format(cont, soma))

# ex 51
primeiro = int(input('primeiro termo: '))
razao = int(input('razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('acabou')

# ex 52
num = int(input('digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('\n\033[m o numero {} foi divisivel {} vezes.'.format(num, tot)) # \n\033[m  -> pulei e linha e resetei a cor
if tot == 2:
    print('PRIMO')
else:
    print('não é PRIMO')

# ex 54
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('em que ano a {}a pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('ao todo tivemos {} maiores de idade'.format(totmaior))
print('ao todo tivemos {} menores de idade'.format(totmenor))

# ex 55 (MUITAS DUVIDAS ???????????????????????????????)
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('peso da {}a pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi de {}kg.'.format(maior))
print('o menor peso lido foi de {}kg.'.format(menor))

# ex 56
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('{}a pessoa: '.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [m/f]: ')).strip()
    somaidade += idade  # pra reforçar += é a soma da variavel + ela mesma
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('a media de idade do grupo é: {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('no total, {} mulheres tem menos de 20 anos'.format(totmulher20))
