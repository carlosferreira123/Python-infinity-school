
'''
Implemente um jogo em que o usuário tenta adivinhar um
número aleatório entre 1 e 20, dando dicas se a tentativa é
muito alta ou muito baixa

'''

import random

#Gerando o numero aleatorio
num_secreto = random.randint(1,20)

num = int(input('Digite um número de 1 a 20 :'))

if(num == num_secreto):
    print(f'Acertou! {num} é o numero secreto')
    num = num_secreto

while (num != num_secreto):
    if (num > num_secreto):
        print(f'{num} é maior que o número secreto')
        num = int(input('Digite novamente: '))
    elif (num_secreto > num):
        print(f'{num} menor que o número secreto')
        num = int(input('Digite novamente: '))

else:
    print(f'Acertou! {num} é o numero secreto')