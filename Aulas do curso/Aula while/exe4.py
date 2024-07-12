'''
Crie um programa que solicite ao usuário que digite números
inteiros. 

O programa deve continuar solicitando números até
que a soma dos números pares digitados seja maior que 50.


Ao atingir ou ultrapassar esse limite, o programa deve exibir a
soma total e encerrar.

'''
soma = 0

while True:
    #Lendo o numero
    num = int(input('Digite um número Inteiro: '))

    #Somando os pares
    if (num%2 == 0):
        soma += num
    
    #Se a soma for maior ou igual a 50 (Limite)
    if (soma >= 50):
        print(f'A soma é igual a {soma}, fim da execução!')
        break