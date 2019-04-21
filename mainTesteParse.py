#comando:
#python mainTesteParse.py

#python mainTesteParse.py -h

##python mainTesteParse.py 4 5 add [exemplo]

import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("number1", help = "first number")
	parser.add_argument("number2", help = "second number")
	parser.add_argument("operation", help = "operation")

	args = parser.parse_args()
	print(args.number1)
	print(args.number2)
	print(args.operation)
	'''
	Two types of Arguments:
		1)Positional
		2)Optional:
			-h, --help(show this help mensseger and exit)
	'''
	n1 = int(args.number1)
	n2 = int(args.number2)
	result = None
	if args.operation == "add":
		result = n1+n2

	else:
		print("unsupported operation")

	print(result)

	'''
	To make argument optional just add -- front of
	argument name:
		parser.add_argument("--number1", help = "first number")
		parser.add_argument("--number2", help = "second number")
		parser.add_argument("--operation", help = "operation")


	'''


	print("deu certo")
