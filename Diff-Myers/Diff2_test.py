import unittest
import Diff2

class TestDiff2(unittest.TestCase):
    def test_03(self):
        a_lines = [
            'Line 1',
            'Line 2',
            'Line 3',
            'Line 4',
        ]

        b_lines = [
            'Line 1',
            'Line 2',
            'Line 4',
        ]

        diff = Diff2.myers_diff(a_lines, b_lines)
        print(diff)

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        print("An exception occured")