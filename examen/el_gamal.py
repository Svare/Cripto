
import argparse

def arg_parse():

    parser = argparse.ArgumentParser(description="diffie_hellman", epilog="Developers Jesús Pacheco - Tania Esmeralda")

    parser.add_argument('-a', action='store', default=None, type=int, required=True, help='Alice private key.', dest='a')
    parser.add_argument('-b', action='store', default=None, type=int, required=True, help='Bob private key', dest='b')
    parser.add_argument('-j', '--alpha', action='store', default=None, type=int, required=True, help='Primitive Root (Public Key)', dest='alpha')
    parser.add_argument('-n', '--prime', action='store', default=None, type=int, required=True, help='Prime Number', dest='n')
    parser.add_argument('-v', '--variable', action='store', default=None, type=int, required=False, help='Random Number', dest='v')
    parser.add_argument('--encrypt', action='store_true', default=False, required=False, help='Specify u want 2 encrypt', dest='encrypt')
    parser.add_argument('--decrypt', action='store_true', default=False, required=False, help='Specify u want 2 decrypt', dest='decrypt')
    parser.add_argument('--addressee', action='store', default=None, required=False, help='Specify who u want 2 send the message', dest='addressee')
    parser.add_argument('--mcla', action='store', default=None, required=False, help='Text in clear to send', dest='mcla')
    parser.add_argument('--k-session', action='store', default=None, type=int, required=False, help='Session Key', dest='k_session')
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
    print('{0:^100}'.format('\u03b1 = {0}, n = {1} -> Z({1})'.format(args.alpha, args.n)))
    print()

    print('{0:^100}'.format('KprivA = a = {}'.format(args.a)))
    print('{0:^100}'.format('KprivB = b = {}'.format(args.b)))

    k_pub_A = mod(args.alpha**args.a, args.n)
    k_pub_B = mod(args.alpha**args.b, args.n)

    print()
    print('{0:^100}'.format('KpubA = \u03b1 ^ a mod n = {0} ^ {1} mod {2} = {3}'.format(args.alpha, args.a, args.n, k_pub_A)))
    print('{0:^100}'.format('KpubA = \u03b1 ^ b mod n = {0} ^ {1} mod {2} = {3}'.format(args.alpha, args.b, args.n, k_pub_B)))

    if(args.encrypt):
        if(args.mcla is not None and args.v is not None and args.addressee is not None):
            mcla = mcla_to_num(args.mcla)
            k_session = mod(args.alpha**args.v, args.n)
            if(args.addressee == 'a'):
                cripto = mod((k_pub_A**args.v)*mcla, args.n)
            elif(args.addressee == 'b'):
                cripto = mod((k_pub_B**args.v)*mcla, args.n)
            else:
                print('Destinatario invalido: {}'.format(args.addressee))
            
            print()
            print('{0:^100}'.format('mcla = {0} = {1}'.format(args.mcla.upper(), mcla)))
            print('{0:^100}'.format('k_session = \u03b1 ^ v mod n = {0} ^ {1} mod {2} = {3}'.format(args.alpha, args.v, args.n, k_session)))
            print('{0:^100}'.format('cripto = ({0} ^ v) * Mcla mod n = ({1} ^ {2}) * {3} mod {4} = {5}'.format('KpubA' if args.addressee == 'a' else 'KpubB', k_pub_A if args.addressee == 'a' else k_pub_B, args.v, mcla, args.n, cripto)))
            print()
            print('{0:^100}'.format('[k_session = {0}, cripto = {1}]'.format(k_session, cripto)))
            print()
        else:
            print('no se especifico mcla, v o destinatario')

    elif(args.decrypt):
        if(args.k_session is not None and args.cripto is not None and args.addressee is not None):
            k = mod(args.k_session**int(args.a if args.addressee == 'a' else args.b), args.n)
            _k = modular_multiplicative_inverse(k, args.n) # Inverso de K
            mcla = mod(args.cripto*_k, args.n)

            print()
            print('{0:^100}'.format('K = k_sesion ^ {0} mod n = {1} ^ {2} mod {3} = {4}'.format('a' if args.addressee == 'a' else 'b', args.k_session, args.a if args.addressee == 'a' else args.b, args.n, k)))
            print('{0:^100}'.format('K^-1 = inv(n, K) = inv({0}, {1}) = {2}'.format(args.n, k, _k)))
            print('{0:^100}'.format('Mcla = cripto * k^-1 mod n = {0} * {1} mod {2} = {3}'.format(args.cripto, _k, args.n, mcla)))
            print()
            print('{0:^100}'.format('DESCIFRANDO'))
            print()

            w = mcla
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
        print('Especifica si quieres cifrar o descifrar')