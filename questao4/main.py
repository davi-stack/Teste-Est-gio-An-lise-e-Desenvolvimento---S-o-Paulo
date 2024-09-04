import json

# Abra e carregue o arquivo JSON como um objeto Python
with open('dados.json', 'r') as file:
    dados = json.load(file)

soma = 0
for elem in dados['faturamento']:
    soma += elem['value']

for elem in dados['faturamento']:
    print(f"O estado {elem['estado']} representa {elem['value']/soma*100:.2f}% do faturamento total")