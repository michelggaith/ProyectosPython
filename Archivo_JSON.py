
''' import json

with open('doc.txt') as file:
    data = json.load(file)

if (data['Cliente']):
    print('data encontrada')
    print(f'{data["Cliente"]}')
else:
    print('No se encontro dicho cliente')
SOLUCION DEL PROFESOR
import json

with open('doc.txt') as file:

data = json.load(file)

print(data)

'''
import json

with open('doc.txt') as file:
  data=json.load(file)
  
print(data)

try:
  if data['clientes1']:
    print('Data encontrada')
    print(f' Clientes 1: {data["clientes1"]}')
  else :
    print('No se encontro dicho cliente')
except KeyError:
  print('Indice no encontrado')