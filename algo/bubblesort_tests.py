import unittest
import bubblesort

class BubblesortTests(unittest.TestCase):

    def test_bubblesort01(self):
        input_list = [12, 28, -1, -5, 24, 39, 17]
        output_list = bubblesort.sort(input_list)
        self.assertEqual(output_list[0], -5)
        self.assertEqual(output_list[1], -1)
        self.assertEqual(output_list[2], 12)
        self.assertEqual(output_list[3], 17)
        self.assertEqual(output_list[4], 24)
        self.assertEqual(output_list[5], 28)
        self.assertEqual(output_list[6], 39)

if __name__ == '__main__':
    unittest.main()
