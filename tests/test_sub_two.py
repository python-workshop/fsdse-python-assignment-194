from unittest import TestCase


class TestSub_two(TestCase):
    def test_sub_two(self):
        try:
            from build import sub_two
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, sub_two, None)
        self.assertEqual(sub_two(7, 5), 2)
        self.assertEqual(sub_two(-5, -7), 2)
        self.assertEqual(sub_two(-5, 7), -12)
        self.assertEqual(sub_two(5, -7), 12)
