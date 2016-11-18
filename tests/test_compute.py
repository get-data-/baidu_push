# -*- coding: utf-8 -*-
import sys
import unittest
from pathlib import Path

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)
from baidu.compute import *


class Parse_URLs(unittest.TestCase):

    def setUp(self):
        self.uri = 'http://www.example.com/en-us/'
    def test_can_parse_domain_name(self):
    	self.assertNotEqual(nameParser(self.uri), self.uri)
    	self.assertEqual(nameParser(self.uri), 'example')

class Encoding_URLs(unittest.TestCase):

	def setUp(self):
		self.uri = 'https://zh.example.com/公司/价值观/'
	def test_can_encode_non_english_urls(self):
		self.assertNotEqual(encodeUrl(self.uri), self.uri)


class NextTest(unittest.TestCase):
	
	def test_something(self):
		self.fail('Write more tests')


if __name__ == '__main__':
    unittest.main()