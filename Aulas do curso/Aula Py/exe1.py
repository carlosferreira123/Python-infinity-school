notas =  []

print('---Menu---')

while True:
    print('1. Adicionar Nota;')
    print('2. Remover Ultima Nota')
    print('3. Encerrar Execução E calcular Média;')

    op = input('Digite a Opção Desejada: ')
    print('')

    match op:
        case '1':
            try:
                nota = float(input('Digite a Nota : '))
            except:
                print('Não digite por Extenso!')

            try:
                notas.append(nota)
            except:
                print('Lista de notas Não Existe! Chama o TI!')


        case '2':
            print('Removendo a Última Nota')
            notas.pop()
            print()

        case '3':
            soma_notas = sum(notas)
            qnt_notas = len(notas)
            print(f'A média foi {soma_notas/qnt_notas:.1f}')
            break

        case _:
            print('Opção Inválida! Burrão!')
            continue