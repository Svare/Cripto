
import argparse
from functools import reduce

def arg_parse():

    parser = argparse.ArgumentParser(description="Linear Feedback Shif Register",
                                        epilog="Desarrolladores Jesús Pacheco - Tania Esmeralda")
    parser.add_argument('-s', '--seed', default=None, type=str, required=True, dest='seed', help='Seed to be used.')
    parser.add_argument('-n', '--nums-to-gen', default=5, type=int, dest='n', help='Numbers to be generated.')
    parser.add_argument('-l', '--left', default=False, dest='left', action='store_true',
                            help='Indicate you want the shift to the left, if not specified default right shift')
    parser.add_argument('-p', '--polynomial', default=None, type=int, required=True, dest='polynomial', nargs='+',
                            help='Polynomial exponents list.')
    
    return parser.parse_args()

def xor(a, b):

    '''
        Calcula la xor de dos cadenas '0' o '1'.
    '''

    return '0' if a == b else '1'
 
def shift(value, bits_to_xor, left):

    '''
        Es el motor del programa aqui se van calculando los numeros
        aleatorios haciendo corrimentos a la izquierda o a la derecha
        dependiendo de la bandera -l recibida desde consola.
    '''
    
    tmp = list(value)
    bit = reduce(xor, bits_to_xor)
    
    if not left:
        tmp.pop()
        tmp.insert(0, bit)
    else:
        tmp.pop(0)
        tmp.append(bit)
    
    return reduce(lambda x,y: x + y, tmp)

def get_taps(value, polynomial):

    '''
        Esta funcion se encarga de calcular los bits que van a ser
        operados por la xor, los extrae le value tomando en cuenta
        los indices en polynomial pero al indice se le resta 1 por
        que en el programa se consideran indices desde 0.
    '''
    
    tmp_str_lst = list(value)
    tmp_bit_lst = []
    
    for element in polynomial:
        tmp_bit_lst.append(tmp_str_lst[element - 1])
    
    return tmp_bit_lst

def gen_num_str(seed_len):

    '''
        Esta funcion lo unico que hace es generar una cadena de numeros consecutivos.
        Ejemplo:
            Recibe 5
            Regresa '12345'
    '''
    return reduce(lambda x,y: x + y, map(lambda x: str(x), list(range(seed_len + 1))[1:]))
 
if __name__ == '__main__':
    
    opts = arg_parse()
    tmp = opts.seed
    
    print('\n{0:^6} {1:^15} {2:^3} {3:^10}\n'.format('Xi', '0x' + gen_num_str(len(opts.seed)), 'XOR', '  Decimal'))

    for i in range(opts.n):
        print('{0:^6} {1:^15} {2:^3} {3:^10}'.format('X' + str(i), '0x' + tmp, reduce(xor, get_taps(tmp, opts.polynomial)), int('0b' + tmp, 2)))
        tmp = shift(tmp, get_taps(tmp, opts.polynomial), opts.left)
    print()
