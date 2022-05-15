from unittest import TestCase, main
from first.logic import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('1-3'), -2)

    def test_multi(self):
        self.assertEqual(calculator('5*10'), 50)

    def test_division(self):
        self.assertEqual(calculator('10/5'), 2)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('FDSFJSFsdgdh')
        self.assertEqual('выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3+4')
        self.assertEqual('выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_not_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2*3.0')
        self.assertEqual('выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a + b')
        self.assertEqual('выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()
