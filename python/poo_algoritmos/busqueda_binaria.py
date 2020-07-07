import random
import time

pasos = 0

def busqueda_binaria(lista, comienzo, final, objetivo):
	print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')

	global pasos
	pasos += 1

	if comienzo > final:
		return False

	medio = (comienzo + final) // 2

	if lista[medio] == objetivo:
		return True
	elif lista[medio] < objetivo:
		return busqueda_binaria(lista, medio + 1, final, objetivo)
	else:
		return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == '__main__':

	tamano_de_lista = int(input('De que tamaño será la lista? '))
	objetivo = int(input('Qué número quieres encontrar? '))
	pasos = 0
	start = time.time()
	lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
	end = time.time()
	
	encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

	print(lista)
	print(f'pasos: {pasos}')
	print(f'Ha demorado {round(start - end, 2)} segundos')
	print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')