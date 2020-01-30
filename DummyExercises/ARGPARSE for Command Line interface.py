import argparse
import sys


def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

def main():
    parser = argparse.ArgumentParser(description='Calculator')
    parser.add_argument('--x',type=float, default=1.0,
                        help = 'What is the first number?')
    parser.add_argument('--y',type=float, default=1.0,
                        help = 'What is the second number?')
    parser.add_argument('--operation',type=str, default='sub',
                        help = 'What is the Operation?(Add,Sub,mul,Div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

    
if __name__ == '__main__':
    main()
