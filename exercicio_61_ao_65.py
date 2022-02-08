# ex 61 e 62
print('gerador de PA')
primeiro = int(input('primeiro termo: '))
razao = int(input('razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos voce quer mostrar a mais: '))
print('progressao com {} termos mostrados'.format(total))

# ex 63 fibonacci
n = int(input('quantos termos de fibonacci quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print (' -> fim')

# ex 64
num = cont = soma = 0
num = int(input('digite um valor [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um valor [999 para parar]: '))
print('voce digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))

# ex 65
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('quer continuar? [s/n] ')).upper().strip()[0]
media = soma / quant
print('voce digitou {} numeros e a media foi {}'.format(quant, media))
print('o maior numero foi {} e o menor foi {}'.format(maior, menor))
