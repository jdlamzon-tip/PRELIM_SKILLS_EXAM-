from temperature import Temperature
import unittest

class TestTemperature(unittest.TestCase):

    def test(self):
        with self.assertRaises(ValueError):
            Temperature(-1)

    def test2(self):
        with self.assertRaises(ValueError):
            Temperature()

    def test3(self):
        with self.assertRaises(ValueError):
            Temperature(1, 2)

    def test4(self):
        with self.assertRaises(ValueError):
            Temperature(1)

if __name__ == "__main__":
    unittest.main()