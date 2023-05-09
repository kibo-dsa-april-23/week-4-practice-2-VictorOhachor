import unittest
from string_recursion import String
import io
import sys

class TestString(unittest.TestCase):
    def test_remove_char(self):
        val = String.remove_char('hello', 'l')
        assert val == 'heo'

    def test_to_upper_case(self):
        val = String.to_upper_case('hello')
        assert val == 'HELLO'

    def test_get_index_valid(self):
        val = String.get_index('hello', 'o')
        assert val == 4

    def test_get_index_invalid(self):
        val = String.get_index('hello', 'z')
        assert val == -1

    def test_prune(self):
        val = String.prune('  hello, world      ')
        assert val == 'hello, world'
