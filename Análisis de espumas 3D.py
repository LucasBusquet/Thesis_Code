import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
import glob

#Tkinter es para poder elegir la carpeta con una ventanita
Folder = tk.filedialog.askdirectory()
#Seteo el directorio de trabajo como el que eleji con el tkinter
os.chdir(Folder)
#Busco las direcciones que hay en esa carpeta
Direcciones = glob.glob("*.txt")
Tam = np.size(Direcciones)
Contar = 0
for i in range(Tam):
	x = str(Contar)
	Name = "Intensidad " + x
	#Leo los txt 1 por 1 y me quedo con la columna que tiene la intensidad
	df = pd.read_table(Direcciones[i], skiprows=13, names=['Intensidad'], usecols=[2], decimal=',')
	df['Intensidad'] = pd.to_numeric(df['Intensidad'])
	NR = df.shape[0]
	#Genero una columna de tiempo donde cada fila incrementa por 1 segundo
	X = 1* np.linspace(1, NR, NR)
	df['Tiempo'] = X
	#Lo ploteo para ver si me sirven
	df.plot(x='Tiempo', y='Intensidad', kind='scatter')
	print('¿Queres conservar estos datos? (Y/N)')
	plt.show()
	q1 = input()
	if q1 == 'y' or q1 == 'Y':	
		print('¿Queres cortar los datos? (Y/N)')
		plt.show()
		q2 = input()
		if q2 == 'y' or q2 == 'Y':
				print('Escriba el maximo:')
				t1 = input()
				df = df[df['Tiempo'] < float(t1)]
				df = df.drop('Tiempo', 1)
				df.rename(columns = {'Intensidad':Name}, inplace = True)
		if q2 == 'n' or q2 == 'N':
				df = df.drop('Tiempo', 1)
				df.rename(columns = {'Intensidad':Name}, inplace = True)
		if Contar == 0:
			df1 = df
		else:
			df2 = [df1, df]
			df1 = pd.concat(df2, axis=1, ignore_index=False)
		Contar += 1
	if q1 == 'n' or q1 == 'N':
		pass
print("5")
for i in range(Contar):
	x = str(i)
	Name = "Intensidad " + x
	Minimo = df1.iloc[:,[i]].min()
	Minimo = float(Minimo)
	df1[Name]=df1[Name]- Minimo
	Maximo = df1.iloc[:,[i]].max()
	Maximo = float(Maximo)
	df1[Name]=df1[Name]/Maximo
print("4")
Y = 0 
df = df1.fillna(0)
Z = df1.count(1)
print("3")
for i in range(Contar):
	x = str(i)
	Name = "Intensidad " + x
	Y = Y + df[Name]
print("2")
Promedio = Y/Z
df1['Promedio Intensidades'] = Promedio
NR = df1.shape[0]
X = np.linspace(1,NR,NR)
Contador = 0
Err = np.zeros(Contar, dtype = float)
print("1")
for i in range(Contar):
	x = str(i)
	Name = "Intensidad " + x
	for j in range(NR):
		NanVal = df1.at[j,Name]
		isNaN = np.isnan(NanVal)
		if isNaN == True:
			Contador = Contador + 0
		if isNaN == False:
			Contador =  Contador + 1
	df_err = df1[df1[Name] < Contador]
	Promedio2 = Promedio[:Contador]
	Errores = sum((df_err[Name]-Promedio2)**2)/Contador
	Err[i] = Errores
	Contador = 0
print("0")
N_muestra = np.linspace(1, Contar, Contar)
figure, axis = plt.subplots(1, 2)
axis[1].plot(N_muestra, Err, "1")
plt.title('Intensidad Promedio')
plt.xlabel('Tiempo')
plt.ylabel('Intensidad')

axis[0].plot(X, Promedio,"D")
plt.title('Mean squared value')
plt.xlabel('N° de medicion')
plt.ylabel('Valor de desvio')
print('¿Quiere guardar el grafico y la matriz? (Y/N)')
q3 = input()
if q3 == 'Y' or q3 == 'y':
		print('Inserte el nombre del grafico')
		Nombre = input()
		plt.savefig(os.path.join(Folder, Nombre))
		Nombre = Nombre + ".xlsx"
		df1.to_excel(os.path.join(Folder, Nombre), index = False, header=True)
if q3 == 'N' or q3 == 'n':
		pass
plt.show()
