"""Calculator using docopt

Usage:
  calc_docopt.py <operation> <num1> <num2>
  calc_docopt.py (-h | --help)

Arguments
  <operation> Math Operation
  <num1> First Number
  <num2> Second Number

Options:
  -h --help     Show this screen.

"""
from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version='Calculator with docopt')
    functions = {
        'add': lambda num1, num2: num1 + num2,
        'subtract': lambda num1, num2: num1 - num2,
        'multiply': lambda num1, num2: num1 * num2,
        'divide': lambda num1, num2: num1 / num2
    }

    print functions[args['<operation>']](int(args['<num1>']), int(args['<num2>']))