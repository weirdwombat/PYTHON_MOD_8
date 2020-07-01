import unittest
import half_birthday as hb


class MyTestCase(unittest.TestCase):
    def test_six_months_later(self):
        self.assertEqual(hb.six_months_later(2020, 5, 30), 2020, 11, 29)


if __name__ == '__main__':
    unittest.main()
