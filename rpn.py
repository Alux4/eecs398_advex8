#!/usr/bin/env python3

import operator
import logging

logging.basicConfig(level=logging.DEBUG)

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.floordiv,
	'^': operator.pow,
}

def calculate(arg):
	# stack for calculator
	stack = []

	# tokenize input
	tokens = arg.split()

	# process tokens
	for token in tokens:
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			function = operators[token]
			val2 = stack.pop()
			val1 = stack.pop()
			result = function(val1, val2)
			stack.append(result)
			#return stack[0]
		logging.debug(stack)
	if len(stack) != 1:
		raise TypeError

	return stack.pop()

def main():
		while True:
				result = calculate(input('rpn calc> '))
				print(result)

if __name__ == '__main__':
	main()
