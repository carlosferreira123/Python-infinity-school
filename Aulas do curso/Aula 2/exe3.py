print(f'-----------Celular Iniciando Pela Primeira Vez!-------------')
print('------------'*5)
senha_verdade = input('Crie a sua Senha: ')
nome_verdade = input('Diga seu nome: ')

print('\n'*4) #Quebra de Linha

print(f'-----------Primeiro Login!-------------')
senha_input = input('Senha: ')
nome_input = input('Nome: ')

if(senha_input != senha_verdade):
    print(f'Senha incorreta!')
elif(nome_verdade == nome_input):
    print(f'Bem vinda {nome_input}')
elif(nome_verdade != nome_input):
    print('Nome errado tente novamente.')
else:
    print(f'Bem-Vindo!')
