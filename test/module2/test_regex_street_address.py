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
        postal_code = "3876873775"
        self.assertTrue(postal_code_match(postal_code))

    def test_invalid_postal_code_should_not_match(self):
        postal_code = "28768-73775"
        self.assertFalse(postal_code_match(postal_code))

    def test_phone_with_country_code_match_the_pattern(self):
        phone = "00989172225645"
        self.assertTrue(phone_match(phone))

    def test_phone_with_country_code_match_the_pattern_farsi(self):
        phone = "۰۰۹۸۹۱۷۲۲۲۵۶۴۵"
        self.assertTrue(phone_match(phone))

    def test_phone_with_wrong_number_should_fail_farsi(self):
        phone = "۰۰۹۸۹۱۷۲۲۲۵۶۴۵...."
        self.assertFalse(phone_match(phone))

    def test_phone_with_country_code_and_dash_match_the_pattern(self):
        phone = "+98-917-2225645"
        self.assertTrue(phone_match(phone))

    def test_phone_without_country_code_match_the_pattern(self):
        phone = "09172225645"
        self.assertTrue(phone_match(phone))



