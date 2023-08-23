import unittest
from app.multi import multiplicación
class TestMulti(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multiplicación(2,3), 6)

if __name__ == '__main__':
    unittest.main()