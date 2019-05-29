import argparse

def arg_parse():

    parser = argparse.ArgumentParser(description="el_gamal", epilog="Developers Jesús Pacheco - Tania Esmeralda")

    parser.add_argument('-p', action='store', default=None, type=int, required=True, help='Prime Number.', dest='p')
    parser.add_argument('-q', action='store', default=None, type=int, required=True, help='Prime Number.', dest='q')
    parser.add_argument('-e', action='store', default=None, type=int, required=False, help='Public Key.', dest='e')
    parser.add_argument('-d', action='store', default=None, type=int, required=False, help='Private Key.', dest='d')
    parser.add_argument('--encrypt', action='store_true', default=False, required=False, help='Specify u want 2 encrypt', dest='encrypt')
    parser.add_argument('--decrypt', action='store_true', default=False, required=False, help='Specify u want 2 decrypt', dest='decrypt')
    parser.add_argument('--addressee', action='store', default=None, required=False, help='Specify who u want 2 send the message', dest='addressee')
    parser.add_argument('--mcla', action='store', default=None, required=False, help='Text in clear to send', dest='mcla')
    parser.add_argument('--cripto', action='store', default=None, type=int, required=False, help='Criptogram', dest='cripto')


    return parser.parse_args()

def mod(num, module):
    return num % module

def mcla_to_num(mcla):

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0

    for i in range(-1,(len(mcla)*-1)-1,-1):
        sum += alphabet.find(mcla[i].upper())*len(alphabet)**((i*-1)-1)
    
    return sum

def modular_multiplicative_inverse(number, module):

    for i in range(1, module):

        if (number * i) % module == 1:
            return i
        
    print('Error al calcular k^-1')
    exit()

if __name__ == "__main__":
    
    args = arg_parse()

    print()
    print('{0:^100}'.format('p = {0}, q = {1} -> SECRETOS'.format(args.p, args.q)))
    print()

    n = args.p * args.q

    print('{0:^100}'.format('n = pq = {0}*{1} = {2}'.format(args.p, args.q, n)))

    phi_n = (args.p - 1) * (args.q -1)

    print('{0:^100}'.format('\u03D5(n) = (p-1)(q-1) = ({0}-1)({1}-1) = {2}'.format(args.p, args.q, phi_n)))

    if(args.encrypt):
        if(args.e is not None and args.mcla is not None):

            mcla = mcla_to_num(args.mcla)
            cripto = mod(mcla**args.e, n)

            if(mcla < 0 or mcla > (n-1)):
                print('\n{0:^100}'.format('Error:: 0 \u2264 mcla \u2264 n-1'))
                exit()

            print()
            print('{0:^100}'.format('mcla = {0} = {1}'.format(args.mcla.upper(), mcla)))
            d = modular_multiplicative_inverse(args.e, phi_n)
            print('{0:^100}'.format('d:: {}'.format(d)))
            print()
            print('{0:^100}'.format('cripto = (mcla ^ e) mod n = ({0} ^ {1}) mod {2} = {3}'.format(mcla, args.e, n, cripto)))
            print()
            print('{0:^100}'.format('[cripto = {}]'.format(cripto)))
            print()

            
            

        else:
            print('Falta especificar e o mcla')

    elif(args.decrypt):
        if(args.d is not None and args.cripto is not None):

            mcla = mod(args.cripto**args.d, n)

            print('{0:^100}'.format('mcla = cripto ^ d mod n = {0} ^ {1} mod {2} = {3}'.format(args.cripto, args.d, n, mcla)))
            print()
            print('{0:^100}'.format('DESCIFRANDO'))
            print()

            w = mcla
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            if(w < len(alphabet)):
                print('{0:^100}'.format('{0} :: {1}'.format(w, alphabet[w])))
                print()
            else:

                while('Jaqui'):
                    
                    if(w//len(alphabet) < 26):                    
                        break
                    else:
                        print('{0:^100}'.format('{0}/{1} = {2} ---> Resto = {3} :: {4}'.format(w, len(alphabet), w//len(alphabet), w%len(alphabet), alphabet[w%len(alphabet)])))
                        w = w//len(alphabet)

                print('{0:^100}'.format('{0}/{1} = {2} ---> Resto = {3} :: {4}'.format(w, len(alphabet), w//len(alphabet), w%len(alphabet), alphabet[w%len(alphabet)])))
                print('{0:^100}'.format('{0} :: {1}'.format(w//len(alphabet), alphabet[w//len(alphabet)])))
                print()

        else:
            print('Falta especificar d o criptorama')
    else:
        print('Especifica si quieres cifrar o descifrar')