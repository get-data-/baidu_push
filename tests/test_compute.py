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
        self.encoded = 'https://zh.example.com/%E5%85%AC%E5%8F%B8/%E4%BB%B7%E5%80%BC%E8%A7%82/'
    def test_can_encode_non_english_urls(self):
        self.assertNotEqual(encodeUrl(self.uri), self.uri)
        self.assertEqual(encodeUrl(self.uri), self.encoded)

class Prepare_base_URL_for_Baidu_endpoint(unittest.TestCase):

    def setUp(self):
        self.uri = 'https://zh.example.com/公司/价值观/'
    def test_can_parse_Baidu_site_var(self):
        self.assertEqual(prepSiteUrl(self.uri), 'zh.example.com')

# class URL_Submission_Logic_test(unittest.TestCase):

#     def setUp(self):
#         self.max = 2000
#         self.min = 1
#         self.invalid = 3000

#     def test_input_is_max(self):
#         test_list = []
#         for x in range(self.max):
#             test_list.append('http://www.example.com')
#         self.assertEqual(len(prepData(test_list, self.max)), self.max)

#     def test_input_is_mix(self):
#         test_list = []
#         for x in range(self.min):
#             test_list.append('http://www.example.com')
#         self.assertEqual(len(prepData(test_list, self.min)), self.min)

class NextTest(unittest.TestCase):
    
    def test_something(self):
        self.fail('Write more tests')



if __name__ == '__main__':
    unittest.main()