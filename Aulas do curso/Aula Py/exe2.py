lista_alunos = []
lista_medias = []

while True:
    print('1. Adicionar Aluno!')
    print('2. Remover Último Aluno Adicionado!')
    print('3. Encerrar!')
    op = input('Opção desejada: ')

    match op:
        case '1':
            aluno = input('Nome do Aluno: ')
            media = float(input('Média do Aluno: '))

            lista_alunos.append(aluno)
            lista_medias.append(media)

        case '2':
            lista_alunos.pop()
            lista_medias.pop()
        case '3':
            print('Encerrando execução')
            break
        case _:
            print('Opção Inválida')

print(lista_alunos)
print(lista_medias)

    

for aluno, media in zip(lista_alunos,lista_medias):
    print(f'Aluno: {aluno}')

    if media <= 10 and media >= 7:
        print(f'Média do Aluno: {media}')
        print('Aprovado!')
    elif media >= 0 and media < 7:
        print(f'Média do Aluno: {media}')
        print(f'Reprovado')
    else:
        print(f'Média do Aluno: {media}')
        print('Média Inválida')
