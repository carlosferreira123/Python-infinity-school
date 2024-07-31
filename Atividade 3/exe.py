n1 = int(input('Digite o numero inicial: '))
n2 = int(input('Digite o numero final: '))

soma = 0


for n in range(n1, n2 +1):
    if n % 2 == 0:
       soma = soma + n

if soma == 0:
    print("Não ha numeros pares no intervalo")
else:
    print(f"A soma dos numeros pares é {soma}")
   