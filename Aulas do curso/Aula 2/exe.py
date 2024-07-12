#Faça um Programa que pergunte quanto você ganha por hora e o número de
#horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
#5% para o sindicato, faça um programa que nos dê:
#Salário bruto
#Quanto pagou ao INSS.
#Quanto pagou ao sindicato.
#O salário líquido.

#Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#Salário Bruto : R$
#IR (11%) : R$
#INSS (8%) : R$
#Sindicato ( 5%) : R$
#Salário Liquido : R$

dindin_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Digite quantas horas você trabalhou: '))

salario_bruto = dindin_hora*horas_trabalhadas


ir = 0.11*salario_bruto   #11% = 0.11 = 11/100
inss = 0.08*salario_bruto #8% = 0.08 = 8/100
sindicato = 0.05*salario_bruto #5% = 0.05 = 5/100

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Seu Salário Bruto é: R${salario_bruto:.2f}')
print(f'Seu Salário Líquido é: R${salario_liquido:.2f}')
