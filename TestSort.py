import sys
import time
import Busquedas
import Sorts
from random import randint

def ArregloAleatorio(n_elementos):
	A = []
	for i in range(0,n_elementos):
		A.append(randint(0,n_elementos))
	return A


nombre_algoritmo=sys.argv[1]
n_elementos=int(sys.argv[2])

A = ArregloAleatorio(n_elementos)

inicio = time.time()

if(nombre_algoritmo == 'InsertionSort'):
	Busquedas.InsertSort(A,0,n_elementos)
	fin = time.time()

if(nombre_algoritmo == 'MergeSort'):
	Sorts.MergeSort(A,0,n_elementos-1)
	fin = time.time()

tiempoTranscurrido = (fin-inicio) * 1000

print(str(nombre_algoritmo)+ " " + str(n_elementos) + " " + " " + str(tiempoTranscurrido))