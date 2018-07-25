import unittest
import math_basics

class TestMathBasics(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_basics.add(1, 1), 2)
        self.assertEqual(math_basics.add(2, 1), 3)
        self.assertEqual(math_basics.add(1, 2), 3)
        self.assertEqual(math_basics.add(12, 99), 111)

if __name__ == '__main__':
    unittest.main()
