import main
import unittest


class EquationTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_discriminant_equal_zero(self):
        self.assertEqual(main.solve_quadratic_equation(2, 4, 2), -1)

    def test_a_equal_zero(self):
        self.assertEqual(main.solve_quadratic_equation(0, 6, 8), -8/6)

    def test_discriminant_higher_than_zero(self):
        self.assertEqual(main.solve_quadratic_equation(2, 3, 1), (-0.5, -1))

    def test_discriminant_lower_than_zero(self):
        self.assertEqual(main.solve_quadratic_equation(
            8, 4, 2), 'Дискриминант меньше нуля')

    def test_zeroes(self):
        self.assertEqual(main.solve_quadratic_equation(
            0, 0, 0), 'Деление на ноль')


if __name__ == '__main__':
    unittest.main()
