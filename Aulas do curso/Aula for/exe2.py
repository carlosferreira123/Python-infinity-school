# Digite uma palavra e conte quantas consoantes essa palavra tem:


palavra = input('Digite uma palavra para contar as vogais: ').upper()

# lower(): minusculo
# upper(): maiusculo

vogais = 'AEIOU'
num_vogais = 0

for letra in palavra:
    if letra in vogais:
        num_vogais += 1

print(f'A palavra {palavra.lower()} tem {len(palavra)-num_vogais} consoantes!')