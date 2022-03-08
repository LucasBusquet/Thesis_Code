import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import os
import Funciones as mf

print('Ingrese el directorio:')
Dir = input()
#Arregla la direccion de Windows para que la lea el Paths
Dir = Dir.replace('\\', '/')
#El excel con los datos
print('Ingrese el nombre del excel:')
Excl = input()
#Le cambio el nombre porque el original se va a utilizar mas adelante
Excl1 = Excl + '.xlsx'
path = os.path.join(Dir, Excl1)
# Cargá el excel
df = pd.read_excel(path, names = ['Foto','Area'], usecols = [1,2])

#Crea una carpeta para poner las fotos
Dir = mf.crear_carpeta(Dir)
Dir = Dir.replace('\\', '/')
#Para poder saber bien cuantas veces loopear
print('Ingrese la cantidad de Fotos')
F = input()
F = int(F) + 1
Name = 'Result of ' + Excl + '.tif:'
#Generamos unos vectores para usar en el for
Promedios = []
Contador = []
#Para poder graficar en log es necesario que las barras crezcan tambien de esa forma
#X = 1.005 * np.linspace(1, 50, 50)
#X = 1*np.logspace(np.log10(0.01),np.log10(0.5), 30)
#Va eligiendo los distintos sets de datos, hace un histograma y lo guarda
for x in range(1,F):
    y = str(x)
    Contador.append(x)
    Name1 = Name + y
    Img = Excl + '-' + y + '.png'
    newdf = df[df.Foto == Name1]
    #Nr = newdf.shape[0]
    Prom = np.average(newdf['Area'])
    Promedios.append(Prom)
    newdf1 = newdf.loc[:, ['Area']] / Prom
    newdf1['Area'] = np.log(newdf1['Area'])
    #newdf2 = newdf.loc[:, ['Area']]
    #newdf2['Area'] = np.log(newdf2['Area'])
    #plt.figure()
    #plt.subplot(211)
    newdf1.hist('Area', density = True, bins = 25)
    plt.ylim(0, 0.5)
    plt.ylabel('N° de burbujas/N° de Burbujas total ')
    plt.xlabel('log(A/<A>)')
    #plt.subplot(212)
    #newdf2.hist('Area', density = True, bins = 20)
    #plt.ylim(0, 0.5)
    plt.savefig(os.path.join(Dir, Img))
    plt.cla()
    plt.close()

plt.plot(Contador, Promedios, 'ro')
plt.ylabel('Area')
plt.xlabel('N° de foto')
plt.savefig(os.path.join(Dir, 'Area'))
plt.show()
