from unittest import TestCase, main
from first.logic import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('2-2'), 0)

    def test_multi(self):
        self.assertEqual(calculator('5*10'), 50)

    def test_division(self):
        self.assertEqual(calculator('10/5'), 2)



if __name__ == '__main__':
    main()
