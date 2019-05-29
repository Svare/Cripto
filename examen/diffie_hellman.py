
import argparse

def arg_parse():

    parser = argparse.ArgumentParser(description="diffie_hellman", epilog="Developers Jesús Pacheco - Tania Esmeralda")

    parser.add_argument('-a', action='store', default=None, type=int, required=True, help='Alice private key.', dest='a')
    parser.add_argument('-b', action='store', default=None, type=int, required=True, help='Bob private key', dest='b')
    parser.add_argument('-j', '--alpha', action='store', default=None, type=int, required=True, help='Primitive Root (Public Key)', dest='alpha')
    parser.add_argument('-n', '--prime', action='store', default=None, type=int, required=True, help='Prime Number', dest='n')

    return parser.parse_args()

if __name__ == "__main__":
    
    args = arg_parse()

    print()
    print('{0:^100}'.format('\u03b1 = {0}, n = {1} -> Z({1})'.format(args.alpha, args.n)))
    print()
    print('{0:^33}{1:^34}{2:^33}'.format('Alice -> a = {0}'.format(args.a), '','Bob -> b = {0}'.format(args.b)))
    print('{0:^33}{1:^34}{2:^33}'.format('\u03b1 ^ a \u2208 G', 'A envia {} --->'.format(args.alpha**args.a%args.n),'\u03b1 ^ b \u2208 G'))
    print('{0:^33}{1:^34}{2:^33}'.format('{0} ^ {1} mod {2}'.format(args.alpha, args.a, args.n), '<--- B envia {}'.format(args.alpha**args.b%args.n), '{0} ^ {1} mod {2}'.format(args.alpha, args.b, args.n)))
    print()
    print('{0:^33}{1:^34}{2:^33}'.format('(\u03b1 ^ b) ^ a \u2208 G', '','(\u03b1 ^ a) ^ b \u2208 G'))
    print('{0:^33}{1:^34}{2:^33}'.format('{0} ^ {1} mod {2}'.format(args.alpha**args.b%args.n, args.a, args.n), '', '{0} ^ {1} mod {2}'.format(args.alpha**args.a%args.n, args.b, args.n)))
    print('{0:^33}{1:^34}{2:^33}'.format((args.alpha**args.b%args.n)**args.a%args.n, '', (args.alpha**args.a%args.n)**args.b%args.n))
    print()
    print('{0:^100}'.format('K = {}'.format((args.alpha**args.b%args.n)**args.a%args.n)))
    print()
