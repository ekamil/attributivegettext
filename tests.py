from collections import UserString
from io import BytesIO
from unittest import TestCase

from translations import AttributiveTranslations

empty_mo_file = BytesIO(b'\x95\x04\x12\xde'  # magic number, same as gettext.GNUTranslations.LE_MAGIC.to_bytes(4, 'big')
                        b'\x00\x00\x00\x01'  # version
                        b'\x00\x00\x00\x00'  # msgcount
                        b'\x00\x00\x00\x00'  # masteridx
                        b'\x00\x00\x00\x00')  # transidx


class AttributiveTranslationsTest(TestCase):
    def test_value_returned_is_userstring(self):
        value_returned = AttributiveTranslations(empty_mo_file).gettext('foo')
        self.assertIsInstance(value_returned, UserString)
