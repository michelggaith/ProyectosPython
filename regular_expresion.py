import re
#BUSQUEDA DE LOS DATOS DE LAS EXPRESIONES
mi_patron = re.compile('\d\d\d')
print((mi_patron.search('Ta122za')).group())  

if (re.search('\Aa[0-9].*(end|fin)', 'a4 es una marca de fin')):  #Busco mayusculas y minusculas y numeros entre 0 y 9, el asteristico dice que
    print('Se encontro el patron')                                #no importa que siga despues, y tiene que tener un fin 

#SUSTITUCIONES

print(re.sub(r'\d', '-', 'hola@g2mail120'))
print(re.sub(r'\d', '', 'hola@g2mail120', 1)) #Count remplaza la cantidad de expresoines indicadas

#MODIFICADORES

reg = re.compile(r'ac', re.IGNORECASE)  #Ignore case ignora el caso que sea, no importa si es mayuscula minuscula, etc
print(reg.search('pedrocualACquierAC'))

def expresion():
    el_patron = re.compile('\d\d\d')
    print(re.search(r'', 'Ta122za'))


expresion()
