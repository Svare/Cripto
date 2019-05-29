import argparse

def arg_parse():

	parser = argparse.ArgumentParser(description="modular_multiplicative_inverse",
										epilog="Developers Jesús Pacheco - Tania Esmeralda")

	parser.add_argument('-m', '--mod', action='store', default=None, type=int, required=True,
							help='module.', dest='module')
	parser.add_argument('-n', '--number', action='store', default=None, type=int, required=True,
							help='number.', dest='number')

	return parser.parse_args()

def modular_multiplicative_inverse(number, module):

    for i in range(1, module):

        if (number * i) % module == 1:
            return i
        
    return -1
        
if __name__ == "__main__":

    args = arg_parse()

    print(modular_multiplicative_inverse(args.number, args.module))

    

