import regex

rulebase = [([
                 ("STREET_ADDRESS",
                  regex.compile('^[\u0600-\u06FF]+(?:[\s0-9()،,-]+[\u0600-\u06FF]+)*$', regex.IGNORECASE), None, None,
                  None),
                 ("STREET_ADDRESS", regex.compile("^([1|3-9][1-9][1-9][1-9][1|6-9]\-?[1-9][1-9][1-9][1-9][1-9])|([1|3-9][1-9][1-9][1-9][5][-]\d{1-3})$", regex.IGNORECASE), None, None, None),
                 ("PHONE", regex.compile("^(0098|\+98)?\-?\s?(0?\d{2})\-?\s?(\d{8})$"), None, None, None),
                 ("PHONE", regex.compile("^(0098|\+98)?\-?\s?(0?9\d{2})\-?\s?(\d{7})$"), None, None, None),
                 ("PHONE", regex.compile("^(\u06F0\u06F0\u06F9\u06F8|\+\u06F9\u06F8)?\-?\s?(\u06F0?[\u06F0-\u06F9]{2})\-?\s?([\u06F0-\u06F9]{8})$"), None, None, None),
             ], 1), ]


def street_address_match(str):
    addr_regex = rulebase[0][0][0][1]
    addr_match = regex.match(addr_regex, str)
    return addr_match and addr_match.string == str


def postal_code_match(str):
    postal_code_regex = rulebase[0][0][1][1]
    postal_code_match = regex.match(postal_code_regex, str)
    return postal_code_match and postal_code_match.string == str


def phone_match(str):
    phone_regex_1 = rulebase[0][0][2][1]
    phone_match_1 = regex.match(phone_regex_1, str)
    phone_regex_2 = rulebase[0][0][3][1]
    phone_match_2 = regex.match(phone_regex_2, str)
    phone_regex_3 = rulebase[0][0][4][1]
    phone_match_3 = regex.match(phone_regex_3, str)
    return (phone_match_1 and phone_match_1.string == str) or \
           (phone_match_2 and phone_match_2.string == str) or \
           (phone_match_3 and phone_match_3.string == str)


if __name__ == "__main__":
    addr = "تهران - خیابان سهروردی - بزرگراه 19 شرقی، کوچه 59, پلاک 39525، طبقه ٣"
    addr_regex = rulebase[0][0][1][1]
    addr_match = regex.match(addr_regex, addr)
    print(addr_match and addr_match.string == addr)

# resources for street address:
# https://stackoverflow.com/questions/41441308/regex-for-accepting-persian-characters-in-address
# postal code: https://stackoverflow.com/questions/48719799/iranian-postal-code-validation
