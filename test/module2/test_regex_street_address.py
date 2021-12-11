from unittest import TestCase

from src.module2.regex_street_address import *


class Test(TestCase):
    def test_street_address_regex_match(self):
        addr = "تهران - خیابان سهروردی - بزرگراه 19 شرقی، کوچه 59, پلاک 39525، طبقه ٣"
        self.assertTrue(street_address_match(addr))


    def test_street_address_regex_does_not_match_wrong_address(self):
        addr = "تهران - خیابان سهروردی - بزرگراه 19 شرقی، کوچه 59, پلاک 39525،// طبقه ٣"
        self.assertFalse(street_address_match(addr))

    def test_postal_code_regex_match(self):
        postal_code = "98768-70775"
        self.assertTrue(postal_code_match(postal_code))

    def test_phone_with_country_code_match_the_pattern(self):
        phone = "00989172225645"
        self.assertTrue(phone_match(phone))

    def test_phone_without_country_code_match_the_pattern(self):
        phone = "09172225645"
        self.assertTrue(phone_match(phone))



