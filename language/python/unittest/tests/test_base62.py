import unittest
from base62 import to_base62


class Base62UnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_base62_to(self):
        self.assertEquals(to_base62(0), '0')
        self.assertEquals(to_base62(62), '10')
        self.assertEquals(to_base62(120), '1W')
        self.assertEquals(to_base62(1597999069), '1K92yx')
        self.assertEquals(to_base62(2597129069), '2PLhUx')
