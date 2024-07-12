#Calcule o fatorial de um numero 
# 5! = 5*4*3*2*1 = 1*2*3*4*5
# 7! = 7*6*5*4*3*2*1
fatorial = 1
numero = int(input('Digite o número que deseja calcular o fatorial: '))

for num in range(1,numero+1):
    fatorial *= num
    # fatorial = fatorial*num

print(f'{numero}! = {fatorial}')