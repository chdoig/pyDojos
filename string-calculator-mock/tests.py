#!/usr/bin/env python

import unittest
import mock
from kata import *

class TestKata(unittest.TestCase):
    def setUp(self):
        self.calc = CommandLineStringCalculator()
        
    def test_suma_cadena(self):
		self.assertEqual(self.calc.parse_args(""), 0)
		

if __name__ == '__main__':
    unittest.main()

