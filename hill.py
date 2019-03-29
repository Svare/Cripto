
#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################
# Afín                           #
# Pacheco Franco Jesús Enrique   #
# Salazar Virgen Tania Esmeralda #
##################################

import sympy
import argparse
from math import trunc

def arg_parse():

	parser = argparse.ArgumentParser(description="Hill",
										epilog="Desarrolladores Jesús Pacheco - Tania Esmeralda")

	parser.add_argument('-k', '--key', action='store', default=None, type=str, required=True,
							help='Word you want to use as key.', dest='key')
	parser.add_argument('-d', '--dim', action='store', default=None, type=int, required=True,
							help='Dimension of the square matrix', dest='dim')
	parser.add_argument('-s', '--string', action='store', default=None, type=str, required=True,
							help='String you want to encrypt or decrypt.', dest='s')
	parser.add_argument('--alphabet', default='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789', type=str, help='Alphabet to be used.')
	parser.add_argument('--decrypt', action='store_true', default=False, help='Default encrypt, if specified decrypt.', dest='decrypt')

	return parser.parse_args()

def split_list(l, dim):

	'''
		Convierte una lista (l) en un arreglo de listas de
		dimension (dim).
	'''

	matrix = []

	for i in range(dim):
		matrix.append(list(l[i*dim:(i+1)*dim].upper()))

	return matrix

def char_to_number(l, alphabet, dim):

	'''
		Convierte una lista de listas de caracteres en una
		lista de listas de numeros, dado un cierto alfabeto
		y una dimension.
	'''

	for i in range(dim):
		for j in range(dim):
			l[i][j] = alphabet.find(l[i][j])

	return l

def polish_string(len_key, string):

	while len(string) < len_key:
		string += "X"
	
	return string[:len_key]


def encrypt(string, key, alphabet, dim):

	crypto = ""

	string = polish_string(len(key), string)

	string = sympy.Matrix(char_to_number(split_list(string, dim), alphabet,dim))
	key = sympy.Matrix(char_to_number(split_list(key, dim), alphabet,dim))

	string = string.T # Es la matriz transpuesta por que el mensaje va al reves

	# Calculamos el inverso multiplicativo y en caso de no ser entero no se
	# puede usar la clave proporcionada para cifrar, entonces se termina la
	# ejecucion del programa.

	aI = (len(alphabet) + 1) / (key.det() % len(alphabet))

	if((aI - trunc(aI)) > 0):
		print("No es posible utilizar esa clave para cifrar!!!")
		exit(0)

	M = string*key # Se otiene la multiplicacion de las matrices

	# Se calcula el modulo de cada elemento de la matriz con el tamaño del
	# alfabeto, se usa la matriz traspuesta de la multiplicacion por que 
	# el criptograma se forma tomando columna por columna.

	crypto_lst = list(map(lambda x: x%len(alphabet), M.T))

	# Se obtiene la letra correspondiente

	for i in crypto_lst:
		crypto += alphabet[i]

	return crypto

def decrypt(crypto, key, alphabet, dim):

	msg = ""

	# Se convienten las cadenas de entrada a matrices cuadradas de numeros
	# los cuales son la posicion de la letra en el alfabeto.

	key = sympy.Matrix(char_to_number(split_list(key, dim), alphabet, dim))
	crypto = sympy.Matrix(char_to_number(split_list(crypto, dim), alphabet, dim))

	print(crypto)

	# Se usa la transpuesta del criptograma por que este se obtiene
	# a partir de las columnas de una matriz.

	crypto = crypto.T

	# Obtenemos la matriz de cofactores transpuesta de nuestra llave,
	# tambien llamada matriz adjunta.

	cofactor_transpose_key = key.adjugate()

	# Se calcula el inverso multiplicativo

	aI = (len(alphabet) + 1) / (key.det() % len(alphabet))

	# Se multiplica la matriz adjunta por el inverso multiplicativo
	# y posteriormente se obtiene una lista que es el resultado de
	# aplicar la operacion modulo n a cada uno de los elementos de
	# la matriz.

	keyM = cofactor_transpose_key*aI
	keyM = list(map(lambda x: x%len(alphabet), keyM))

	# Se vuelve a construir una matriz a partir de la lista obtenida
	# anteriormente para poder multiplicarla por el criptograma.

	keyI = []

	for i in range(dim):
		keyI.append(list(keyM[i*dim:(i+1)*dim]))

	# Del resultado de la multiplicacion del criptograma por la llave
	# inversa se obtiene la matriz transpuesta por que el mensaje se
	# lee de las columnas, y de cada elemento de esa lista se obtiene
	# el modulo n que corresponde a el numero de caracter del alfabeto
	# entonces ya con ese numero simplemente vamos concatenando hasta
	# obtener el mensaje.

	for j in list((crypto*sympy.Matrix(keyI)).T):
		msg += alphabet[j%len(alphabet)]

	return msg

if __name__ == '__main__':

	args = arg_parse()

	if not args.decrypt:
		print(encrypt(args.s, args.key, args.alphabet, args.dim))
	else:
		print(decrypt(args.s, args.key, args.alphabet, args.dim))