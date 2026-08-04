# pylint: disable-all
import unittest
from demo import hello_world

class TestDemo(unittest.TestCase):
    def test_returns_hello_world(self):
        self.assertEqual("Hello World!", hello_world())
