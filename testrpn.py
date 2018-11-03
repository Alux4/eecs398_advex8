import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 + 2 +')
		self.assertEqual(2, result)

	def test_subtract(self):
		result = rpn.calculate('7 4 -')
		self.assertEqual(3, result)

	def test_multiply(self):
		result = rpn.calculate('9 4 *')
		self.assertEqual(36, result)

	def test_divide(self):
		result = rpn.calculate('48 12 /')
		self.assertEqual(4, result)

	def test_too_many(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('1 2 3 +')
