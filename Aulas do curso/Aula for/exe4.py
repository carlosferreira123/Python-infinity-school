# Digite uma palavra e conte quantas vogais essa palavra tem


palavra = input('Digite uma palavra para contar as vogais: ')
vogais = 'aeiou'
num_vogais = 0

for letra in palavra:
    if letra in vogais:
        num_vogais += 1

print(f'A palavra {palavra} tem {num_vogais} vogais!')