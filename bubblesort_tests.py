import unittest
import bubblesort

class BubblesortTests(unittest.TestCase):

    def test_bubblesort01(self):
        input_list = [12, 28, -1, -5, 24, 39, 17]
        output_list = bubblesort.sort(input_list)
        self.assertEqual(output_list[0], 2)
        self.assertEqual(output_list[1], 3)
        self.assertEqual(output_list[2], 1)

if __name__ == '__main__':
    unittest.main()
