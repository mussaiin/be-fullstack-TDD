from unittest import TestCase

import find_max as f

class FindMaxTest(TestCase):
    def test_get_max(self):
        result = f.get_max(1, 34)
        self.assertEqual(result, 34)

    def test_get_max_without_arguments(self):
        self.assertRaises(TypeError, f.get_max_without_arguments)

    def test_get_max_with_one_argument(self):
        result = f.get_max_with_one_argument(123)
        self.assertEqual(result, 123)

    def test_get_max_with_many_arguments(self):
        result = f.get_max_with_many_arguments(1, 2, 3, 4)
        self.assertEqual(4, result)

    def test_get_max_with_one_or_more_arguments(self):
        first = 124
        array = [1123, 1421, 12]
        result = f.get_max_with_one_or_more_arguments(first, *array)
        self.assertEqual(1421, result)

    def test_get_max_bounded(self):
        pass

    def test_make_max(self):
        pass
