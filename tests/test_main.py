import unittest
from app.main import say_hello

class TestMain(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("World"), "Hello, World!")
        self.assertEqual(say_hello("Alice"), "Hello, Alice!")

if __name__ == '__main__':
    unittest.main()
