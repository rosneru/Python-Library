import unittest
import file_tools

class TestFileTools(unittest.TestCase):

    def test_create_name_for_insert(self):
        old_name = "myOldClassName"

        new_name_1 = file_tools.create_name_for_insert(old_name, "New", 2)
        new_name_2 = file_tools.create_name_for_insert(old_name, "New", 1)
        new_name_3 = file_tools.create_name_for_insert(old_name, "New", 0)
        new_name_4 = file_tools.create_name_for_insert(old_name, "New", 9)
        new_name_5 = file_tools.create_name_for_insert(old_name, "New", 13)
        new_name_6 = file_tools.create_name_for_insert(old_name, "New", 14)
        new_name_7 = file_tools.create_name_for_insert(old_name, "New", 15)
        new_name_8 = file_tools.create_name_for_insert(old_name, "New", 35)
        
        self.assertEqual(new_name_1, "myNewOldClassName")
        self.assertEqual(new_name_2, "mNewYOldClassName")
        self.assertEqual(new_name_3, "NewMyOldClassName")
        self.assertEqual(new_name_4, "myOldClasNewSName")
        self.assertEqual(new_name_5, "myOldClassNamNewE")
        self.assertEqual(new_name_6, "myOldClassNameNew")
        self.assertEqual(new_name_7, "myOldClassNameNew")
        self.assertEqual(new_name_8, "myOldClassNameNew")

if __name__ == '__main__':
    unittest.main()
