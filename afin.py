
#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################
# Afín                           #
# Pacheco Franco Jesús Enrique   #
# Salazar Virgen Tania Esmeralda #
##################################

import argparse

def arg_parse():

	parser = argparse.ArgumentParser(description="Afín [Valores defecto César]",
										epilog="Desarrolladores Jesús Pacheco - Tania Esmeralda")

	parser.add_argument('-a', default = 1, type=int, help='Decimation Constant.')
	parser.add_argument('-b', default = 3, type=int, help='Displacement Constant.')
	parser.add_argument('-k', '--key', action='store', default=None, type=str, required=False,
							help='The key you want to use.', dest='key')
	parser.add_argument('-n', action='store', default=37, type=int, help='Number of alphabet symbols.')
	parser.add_argument('-s', '--string', action='store', default=None, type=str, required=True,
							help='String you want to encrypt or decrypt.', dest='s')
	parser.add_argument('--alphabet', default='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789', type=str, help='Alphabet to be used.')
	parser.add_argument('--decrypt', action='store_true', default=False, help='Default encrypt, if specified decrypt.', dest='decrypt')

	return parser.parse_args()

def _ai_(a, n):

	for b in range(n):
		x = (a*b)%n;
		if x == 1:
			return b

	return 0

def polish_key(key, length):

	polished_key = ""
	j = 0

	for i in range(length):
		j = 0 if j == len(key) else j
		polished_key += key[j]
		j+=1

	return polished_key

def encrypt(a, b, n, string, key, alphabet):
	
	crypto = ''

	if key is not None:
		if len(key) >= len(string):
			for i in range(len(string)):
				crypto += alphabet[(alphabet.find(string[i])*a + alphabet.find(key[i])) % n]
		else:
			key = polish_key(key, len(string))
			for i in range(len(string)):
				crypto += alphabet[(alphabet.find(string[i])*a + alphabet.find(key[i])) % n]
	else:
		for c in string.upper():
			crypto += alphabet[(alphabet.find(c)*a + b) % n]

	return crypto

def decrypt(a, b, n, string, key, alphabet):

	ai = _ai_(a, n)
	plainMsg = ''

	if key is not None:
		if len(key) >= len(string):
			for i in range(len(string)):
				plainMsg += alphabet[(alphabet.find(string[i]) - alphabet.find(key[i]))*ai % n]
		else:
			key = polish_key(key, len(string))
			for i in range(len(string)):
				plainMsg += alphabet[(alphabet.find(string[i]) - alphabet.find(key[i]))*ai % n]
	else:
		for c in string.upper():
			plainMsg += alphabet[(alphabet.find(c) - b)*ai % n]

	return plainMsg

if __name__ == '__main__':

	args = arg_parse()

	if not args.decrypt:
		print(encrypt(args.a, args.b, args.n, args.s, args.key, args.alphabet))
	else:
		print(decrypt(args.a, args.b, args.n, args.s, args.key, args.alphabet))