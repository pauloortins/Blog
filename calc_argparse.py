import argparse

functions = {
	'add': lambda num1, num2: num1 + num2,
	'subtract': lambda num1, num2: num1 - num2,
	'multiply': lambda num1, num2: num1 * num2,
	'divide': lambda num1, num2: num1 / num2
}

parser = argparse.ArgumentParser()
parser.add_argument("operation", help="mathematical operation that will be performed", 
	choices=['add', 'subtract', 'multiply', 'divide'])
parser.add_argument("num1", help="the first number", type=int)
parser.add_argument("num2", help="the second number", type=int)
args = parser.parse_args()

print functions[args.operation](args.num1, args.num2)