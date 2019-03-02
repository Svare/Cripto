import argparse

def arg_parse():

	parser = argparse.ArgumentParser(description="Cifrado y Descifrado algoritmo afín",
										epilog="Y pues así brotha")

	parser.add_argument('-a', default = 1, type=int)
	parser.add_argument('-b', default = 3, type=int)
	parser.add_argument('-k', '--key')
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

def encrypt(a, b, n, string, alphabet):
	
	crypto = ''

	for c in string.upper():
		crypto += alphabet[(alphabet.find(c)*a + b) % n]

	return crypto

def decrypt(a, b, n, string, alphabet):

	ai = _ai_(a, n)
	plainMsg = ''

	for c in string.upper():
		plainMsg += alphabet[(alphabet.find(c) - b)*ai % n]

	return plainMsg

if __name__ == '__main__':

	args = arg_parse()

	if not args.decrypt:
		print(encrypt(args.a, args.b, args.n, args.s, args.alphabet))
	else:
		print(decrypt(args.a, args.b, args.n, args.s, args.alphabet))