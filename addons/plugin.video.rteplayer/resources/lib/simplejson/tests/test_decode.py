import decimal
from unittest import TestCase

import simplejson as S

class TestDecode(TestCase):
    def test_decimal(self):
        rval = S.loads('1.1', parse_float=decimal.Decimal)
        self.assert_(isinstance(rval, decimal.Decimal))
        self.assertEquals(rval, decimal.Decimal('1.1'))

    def test_float(self):
        rval = S.loads('1', parse_int=float)
        self.assert_(isinstance(rval, float))
        self.assertEquals(rval, 1.0)
