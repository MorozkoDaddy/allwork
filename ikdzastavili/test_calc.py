import unittest
from calcaska import caca

class Test(unittest.TestCase):

    def calc_sum(self):
        caca.x = 42
        self.assertEqual(caca.calc_sum(6), 12)

    def calc_multiply(self):
        caca.x = 45
        self.assertEqual(caca.calc_multiply(6), 12)
    def calc_substract(self):
        caca.x = 1
        self.assertEqual(caca.calc_substract(6), 12)
    def calc_divide(self):
        caca.x = 4
        self.assertEqual(caca.calc_divide(6), 12)

if __name__ == '__main__':
    unittest.main()