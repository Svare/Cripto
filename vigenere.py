
#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################
# Afín                           #
# Pacheco Franco Jesús Enrique   #
# Salazar Virgen Tania Esmeralda #
##################################

import argparse

def arg_parse():

	parser = argparse.ArgumentParser(description="Vigenere",
										epilog="Desarrolladores Jesús Pacheco - Tania Esmeralda")

	parser.add_argument('-k', '--key', action='store', default=None, type=str, required=True,
							help='Word you want to use as key.', dest='key')
	parser.add_argument('-s', '--string', action='store', default=None, type=str, required=True,
							help='String you want to encrypt or decrypt.', dest='s')
	parser.add_argument('--alphabet', default='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789', type=str, help='Alphabet to be used.')
	parser.add_argument('--decrypt', action='store_true', default=False, help='Default encrypt, if specified decrypt.', dest='decrypt')

	return parser.parse_args()

def encrypt(string, key, alphabet):
	cripto = ""
	i = 0
	for letter in string:
		_sum_ = alphabet.find(letter) + alphabet.find(key[i % len(key)])
		module = int(_sum_) % len(alphabet)
		cripto += str(alphabet[module]) 
		i = i + 1
	return cripto

def decrypt(string, key, alphabet):
	cripto = ""
	i = 0
	for letter in string:
		_sum_ = alphabet.find(letter) - alphabet.find(key[i % len(key)])
		module = int(_sum_) % len(alphabet)
		cripto += str(alphabet[module]) 
		i = i + 1
	return cripto


if __name__ == '__main__':

	args = arg_parse()

	if not args.decrypt:
		print(encrypt(args.s.upper(), args.key.upper(), args.alphabet))
	else:
		print(decrypt(args.s.upper(), args.key.upper(), args.alphabet))