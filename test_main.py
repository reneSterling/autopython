import unittest

from main import add
class Tester(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2,3),5)
    self.assertEqual(add(5,6),11)

if __name__ == '__main__':
  unittest.main()
  
