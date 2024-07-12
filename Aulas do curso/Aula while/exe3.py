import random

num_secreto = random.randint(1,100) # Gerando um número de 1 a 100

palpites = 0

while palpites < 10:
    num = int(input('Digite o seu palpite: '))

    palpites += 1

    if num > num_secreto:
        print(f' O número {num} é maior que o numero secreto')
    elif num < num_secreto :
        print(f' O número {num} é menor que o numero secreto')
    else:
        print(f'Acertou! Numero secreto é {num}')
        break


if (num == num_secreto):
    print(f'Acertou com {palpites} palpites')
else:
    print(f'Numero de tentativas Excedidos! Numero secreto era  {num_secreto}')