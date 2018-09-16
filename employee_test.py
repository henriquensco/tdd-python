import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def test_email(self):
		emp_1 = Employee('Corey', 'Schafer', 50000)
		emp_2 = Employee('Henrique', 'Nascimento', 60000)

		self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
		self.assertEqual(emp_2.email, 'Henrique.Nascimento@email.com')

		emp_1.first = 'Jhon'
		emp_2.first = 'Jane'

		self.assertEqual(emp_1.email, 'Jhon.Schafer@email.com')
		self.assertEqual(emp_2.email, 'Jane.Nascimento@email.com')

	def test_fullname(self):
		emp_1 = Employee('Corey', 'Schafer', 50000)
		emp_2 = Employee('Henrique', 'Nascimento', 60000)

		self.assertEqual(emp_1.fullname, 'Corey Schafer')
		self.assertEqual(emp_2.fullname, 'Henrique Nascimento')

		emp_1.first = 'Jhon'
		emp_2.first = 'Jane'

		self.assertEqual(emp_1.fullname, 'Jhon Schafer')
		self.assertEqual(emp_2.fullname, 'Jane Nascimento')

	def test_apply_raise(self):
		emp_1 = Employee('Corey', 'Schafer', 50000)
		emp_2 = Employee('Henrique', 'Nascimento', 60000)

		emp_1.apply_raise()
		emp_2.apply_raise()

		self.assertEqual(emp_1.pay, 52500)
		self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
	unittest.main()