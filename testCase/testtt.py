import unittest
from ddt import ddt, data, unpack


@ddt
class MyTestCase(unittest.TestCase):

    @data(1, 2, 3)
    def test_something(self, value):
        self.assertEqual(value, 2)


if __name__ == '__main__':
    unittest.main()
