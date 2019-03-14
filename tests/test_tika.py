import unittest

import tika
from tika import parser

class TestXGBoost(unittest.TestCase):
    def test_tika(self):
        image = 'https://raw.githubusercontent.com/nmcteam/image-with-text/master/example/destination.jpg'
        tika.initVM()
        parsed = parser.from_file(image)
