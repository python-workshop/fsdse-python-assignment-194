from unittest import TestCase
import sys



class TestSub_two(TestCase):
    def test_sub_two(self):
        try:
            from build import sub_two
        except:
            self.assertFalse("Function not present")

        self.assertRaises(TypeError, sub_two, None, 5)
        self.assertRaises(ValueError, sub_two, 4, 5)
        linenum = sub_two(6, 5)
        self.assertEqual(1, linenum)