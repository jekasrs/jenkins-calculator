import unittest
from unittest.mock import patch
import utils
from utils import read_number

class TestUserInput(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['not a number','10', '-20'])
    def test_correct_input_number(self, mock_input):
       number = read_number()
       self.assertIsNone(number)
       
       number = read_number()
       self.assertIsInstance(number, int)
       self.assertEqual(number, 10)
       
       number = read_number()
       self.assertIsInstance(number, int)
       self.assertEqual(number, -20)