# Digite uma palavra e conte quantas consoantes essa palavra tem:


palavra = input('Digite uma palavra para contar as vogais: ').lower()

# lower(): minusculo
# upper(): maiusculo

vogais = 'aeiou'
num_consoantes = 0

for letra in palavra:
    if letra not in vogais:
        num_consoantes += 1

print(f'A palavra {palavra} tem {num_consoantes} consoantes!')
