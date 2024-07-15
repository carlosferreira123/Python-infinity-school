convidados = ['Josué Noivo','Leandra Noiva','Tio Bruno']
convidados_bruno = ['Josué Noivo','Leandra Noiva','Jamylle Esposa do Bruno']
print('---- MENU CASAMENTO ----')

while True:
    print('1. Adicionar Convidado dos Noivos')
    print('2. Adicionar Convidado do Tio Bruno')
    print('3. Desconvidar')
    print('4. Lista de Convidados')
    print('5. Remover Convidados Repetidos')
    print('6. Convidar de Verdade os convidados do Tio Bruno.')
    print('7. Casar!')
    op = input('Digite a Opção desejada:')

    match op:
        case '1':
            print('--- ADICIONANDO CONVIDADO ---')
            nome = input('Digite o nome do Convidado: ')
            convidados.append(nome)
            print(f'{nome} Convidado com Sucesso!',end='\n\n')
        case '2':
            print('--- ADICIONANDO CONVIDADO BRUNO ---')
            nome = input('Digite o nome do Convidado do Bruno: ')
            convidados_bruno.append(nome)
        case '3':
            print('--- DESCONVIDANDO ---')
            nome = input('Digite o nome do Desconvidado: ')

            try:
                convidados.remove(nome)
            except:
                print('Convidado Não está na Lista!', end='\n\n')
        
        case '4':
            for i , nome in enumerate(convidados):
                print(f'Convidado {i+1} : {nome}')
            print()

        case '5':
            # Set -> conjunto (não aceita elementos repetidos)
            convidados = list(set(convidados))
        case '6':
            set_convidados = set(convidados)
            set_convidados_bruno = set(convidados_bruno)

            convidados = list(set_convidados.union(set_convidados_bruno))
        case '7':
            print('Lá vem o noivo todo de branco!')
            break
        case _:
            print('Opção inválida!',end='\n\n')