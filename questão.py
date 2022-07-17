
import json


 

with open("dados.json", encoding='utf-8') as my_json:
  dados = json.load(my_json)


soma = sum(i['valor'] for i in dados)
menor = min(i['valor'] for i in dados if i['valor'] != 0)
maior = max(i['valor'] for i in dados)

media = soma/len(dados)


for i in dados:
  d = i['dia']
  v= i['valor']
  if i['valor'] > media:
    print(f'Faturamento maíor que a média Dia: {d} - Faturamento: R${v}')    

for i in dados:
  d = i['dia']
  v= i['valor']
  if i['valor'] == maior:
    print(f'\nMaior faturamento foi dia: {d} - faturamento: R${v}\n')

for i in dados:
  d = i['dia']
  v= i['valor']
  if i['valor'] == menor:
    print(f'\nMenor faturamento foi dia: {d} - faturamento: R${v}\n')







  
  






