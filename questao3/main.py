import json

# Abra e carregue o arquivo JSON como um objeto Python
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Agora você pode acessar e manipular os dados como um objeto Pythonv
vetor = dados['faturamento_diario']
menor = 0
maior = vetor[0]['valor']

soma = 0
for elem in vetor:
    soma += elem['valor']
media = soma/len(vetor)
num = 0 #numero de mês com média maior que a média
for elem in vetor:
    # print(elem['valor'])
    if elem['valor'] < menor:
        menor = elem['valor']
    if elem['valor'] > maior:
        maior = elem['valor']
    if elem['valor'] > media:
        num += 1
print(f'O menor faturamento diário foi de R${menor}')
print(f'O maior faturamento diário foi de R${maior}')
print(f'A média de faturamento diário foi de R${media:.2f}')
print(f'{num} meses tiveram faturamento diário acima da média')