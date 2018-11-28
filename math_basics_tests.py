import unittest
import math_basics

class TestMathBasics(unittest.TestCase):

    def test_ggT(self):
        self.assertEqual(math_basics.ggT(360, 945), 45)
        self.assertEqual(math_basics.ggT(945, 360), 45)
        self.assertEqual(math_basics.ggT(81, 98), 1)
        self.assertEqual(math_basics.ggT(98, 81), 1)

if __name__ == '__main__':
    unittest.main()
