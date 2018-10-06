from unittest import TestCase

import find_max as f

class FindMaxTest(TestCase):
    def test_get_max(self):
        result = f.get_max(1, 34)
        self.assertEqual(result, 34)

    def test_get_max_without_arguments(self):
        self.assertRaises(TypeError, f.get_max_without_arguments)

    def test_get_max_with_one_argument(self):
        pass

    def test_get_max_with_many_arguments(self):
        pass

    def test_get_max_with_one_or_more_arguments(self):
        pass

    def test_get_max_bounded(self):
        pass

    def test_make_max(self):
        pass
