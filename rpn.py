#!/usr/bin/env python3

import operator
import logging
import readline
from colorama import Fore, Back, Style

logging.basicConfig(level=logging.DEBUG)

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
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
		logging.debug(Fore.YELLOW + str(stack))
		print(Style.RESET_ALL)
	if len(stack) != 1:
		raise TypeError("Too many parameters")

	return stack.pop()

def main():
		while True:
				result = calculate(input('rpn calc> '))
				print(Fore.GREEN + str(result))
				print(Style.RESET_ALL)

if __name__ == '__main__':
	main()
