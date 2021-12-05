from unittest import TestCase

from src.module2.regex_street_address import street_address_match, postal_code_match


class Test(TestCase):
    def test_street_address_regex_match(self):
        addr = "تهران - خیابان سهروردی - بزرگراه 19 شرقی، کوچه 59, پلاک 39525، طبقه ٣"
        self.assertTrue(street_address_match(addr))


    def test_street_address_regex_does_not_match_wrong_address(self):
        addr = "تهران - خیابان سهروردی - بزرگراه 19 شرقی، کوچه 59, پلاک 39525،// طبقه ٣"
        self.assertFalse(street_address_match(addr))

    def test_postal_code_regex_match(self):
        postal_code = "9876870773"
        self.assertTrue(postal_code_match(postal_code))
