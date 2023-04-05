import zipfile
from zipfile import ZipFile

with zipfile.ZipFile('archivo.zip', w) as fzip:
    fzip.write('doc.txt')
    #Genero un archivo zip y guardo el documento
    fzip.printdir()         # me muestra los datos del mismo
    fzip.extractall()       #Extrae los documentos

# PARA GZIP se usa: (es de linux)

import gzip

with open('python.docx', 'rb') as file:
    with gzip.open('fichero.txt.gz', 'wb') as fichero:
        fichero.writelines(file)

#Formato TAR
import tarfile

file_tar = tarfile.open('doc.txt', 'w.gz')
file_tar.add('doc.txt')
file_tar.close()