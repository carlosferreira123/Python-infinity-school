'''
Digite 15 notas e calcule a média
'''

contador = 0
soma_notas = 0

while (contador < 15):
    nota = float(input(f'Digite a {contador+1} nota: '))
    
    soma_notas += nota

    contador += 1


media = soma_notas/15

print(f'A sua média foi {media:.2f}')